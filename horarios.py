# horarios.py
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 13:51:31 2025
@author: Maria Almeida Pizarro
"""

import pandas as pd
import matplotlib.pyplot as plt
import unicodedata
from datetime import datetime

# === 1. CARGA Y LIMPIEZA DE DATOS ===

materias = pd.read_excel("materias_ofertadas.xlsx")
pensum = pd.read_excel("pensum_academico_usc.xlsx")
contactos_df = pd.read_excel("FACULTADES.xlsx")

# Normalizar nombres de columnas
materias.rename(columns={'HORARIO_FIN': 'HORA_FIN'}, inplace=True)
materias.columns = materias.columns.str.strip().str.upper().str.replace(' ', '_')
print("🧾 Nombres reales de columnas:")
print(materias.columns.tolist())

# Agrupación limpia
materias_agrupadas = materias.groupby(['ASIGNATURA', 'GRUPO']).agg({
    'PROGRAMA': 'first',
    'PENSUM': 'first',
    'NIVEL': 'first',
    'AULA': 'first',
    'CUPO': 'first',
    'INSCRITOS': 'first',
    'DOCENTE': 'first',
    'DIA': lambda x: ', '.join(sorted(set(x.dropna().astype(str)))),
    'HORA_INICIO': lambda x: ', '.join(sorted(set(x.dropna().astype(str)))) if 'HORA_INICIO' in materias.columns else '',
    'HORA_FIN': lambda x: ', '.join(sorted(set(x.dropna().astype(str)))) if 'HORA_FIN' in materias.columns else ''
}).reset_index()

# === 2. UTILIDADES ===

def normalizar_texto(texto):
    if isinstance(texto, str):
        texto = texto.strip().upper()
        texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
    return texto

def limpiar_input_opciones(valor, opciones):
    valor = normalizar_texto(valor)
    for clave, lista in opciones.items():
        if valor in lista:
            return clave
    return valor

def horas_solapan(hora_ini1, hora_fin1, hora_ini2, hora_fin2):
    try:
        fmt = "%H:%M:%S" if ":" in str(hora_ini1) and len(str(hora_ini1).split(":")) == 3 else "%H:%M"
        h1_ini = datetime.strptime(str(hora_ini1), fmt)
        h1_fin = datetime.strptime(str(hora_fin1), fmt)
        h2_ini = datetime.strptime(str(hora_ini2), fmt)
        h2_fin = datetime.strptime(str(hora_fin2), fmt)
        return max(h1_ini, h2_ini) < min(h1_fin, h2_fin)
    except Exception as e:
        print("⛔ Error comparando horas:", e)
        return False

# === 3. RECOMENDADOR DE HORARIOS ===

def recomendar_horarios(pensum, materias_agrupadas):
    pensum.columns = pensum.columns.str.strip().str.upper()
    materias_agrupadas.columns = materias_agrupadas.columns.str.strip().str.upper()
    pensum['MATERIA_NORM'] = pensum['MATERIA'].apply(normalizar_texto)
    pensum['CARRERA_NORM'] = pensum['CARRERA'].apply(normalizar_texto)
    materias_agrupadas['ASIGNATURA_NORM'] = materias_agrupadas['ASIGNATURA'].apply(normalizar_texto)

    print("🔷 Bienvenido al recomendador de materias inteligentes 🔷\n")
    programa_input = input("🎓 ¿Qué programa estudias?: ")
    semestre_input = int(input("📚 ¿En qué semestre vas?: "))
    jornada_input = input("⏰ ¿Prefieres estudiar en la MAÑANA, TARDE o TODO EL DÍA?: ")
    dia_excluido_input = input("📅 ¿Hay algún día que quieras evitar (ej. VIERNES, SÁBADO)? Si no, deja vacío: ")
    agrupado_input = input("📆 ¿Prefieres concentrar materias en pocos días? (S/N): ")

    programa_norm = normalizar_texto(programa_input)
    jornada_opciones = {
        "MANANA": ["MANANA", "MAÑANA", "AM"],
        "TARDE": ["TARDE", "PM"],
        "TODO EL DIA": ["TODO EL DIA", "TODO", "COMPLETO"]
    }
    jornada = limpiar_input_opciones(jornada_input, jornada_opciones)

    dias_opciones = {
        "LUN": ["LUNES", "LUN", "MONDAY"],
        "MAR": ["MARTES", "MAR", "TUESDAY"],
        "MIE": ["MIERCOLES", "MIÉRCOLES", "MIE", "WEDNESDAY"],
        "JUE": ["JUEVES", "JUE", "THURSDAY"],
        "VIE": ["VIERNES", "VIE", "FRIDAY"],
        "SAB": ["SABADO", "SÁBADO", "SAB", "SATURDAY"]
    }

    dia_excluido = ""
    if dia_excluido_input:
        dia_norm = normalizar_texto(dia_excluido_input)
        for clave, lista in dias_opciones.items():
            if dia_norm in lista:
                dia_excluido = clave
                break

    agrupado = agrupado_input.strip().upper() == "S"
    pensum_filtrado = pensum[
        (pensum['CARRERA_NORM'] == programa_norm) & (pensum['SEMESTRE'] == semestre_input)
    ]

    recomendadas = []
    horarios_ocupados = []

    for _, fila in pensum_filtrado.iterrows():
        materia = fila["MATERIA"]
        materia_norm = fila["MATERIA_NORM"]
        oferta = materias_agrupadas[materias_agrupadas["ASIGNATURA_NORM"] == materia_norm]

        if oferta.empty:
            recomendadas.append({
                "ASIGNATURA": materia,
                "GRUPO": "NO OFERTADA",
                "DIA": "—",
                "HORA_INICIO": "—",
                "HORA_FIN": "—",
                "AULA": "—",
                "DOCENTE": "—",
                "NOTA": "📌 No se ofertó este semestre"
            })
            continue

        opciones_compatibles = []
        for _, op in oferta.iterrows():
            hora_ini = op["HORA_INICIO"]
            hora_fin = op["HORA_FIN"]
            if ":" not in str(hora_ini) or ":" not in str(hora_fin):
                continue

            dias_raw = op["DIA"]
            dias_lista = [normalizar_texto(d.strip()) for d in dias_raw.split(",")]

            if dia_excluido and any(dia_excluido == d for d in dias_lista):
                continue

            h_ini_hora = int(str(hora_ini).split(":")[0])
            cumple_jornada = (
                jornada == "TODO EL DIA" or
                (jornada == "MANANA" and h_ini_hora < 12) or
                (jornada == "TARDE" and h_ini_hora >= 12)
            )
            if not cumple_jornada:
                continue

            conflicto = False
            for dia in dias_lista:
                for h in horarios_ocupados:
                    if dia == h["DIA"] and horas_solapan(hora_ini, hora_fin, h["INI"], h["FIN"]):
                        conflicto = True
                        break
                if conflicto:
                    break

            if not conflicto:
                opciones_compatibles.append(op)

        if opciones_compatibles:
            print(f"\n📌 Opciones disponibles para {materia}:")
            for idx, alt in enumerate(opciones_compatibles):
                print(f"{idx + 1}. {alt['DIA']} de {alt['HORA_INICIO']} a {alt['HORA_FIN']} | "
                      f"GRUPO {alt['GRUPO']} | AULA {alt['AULA']} | DOCENTE {alt['DOCENTE']}")

            while True:
                seleccion = input(f"👉 Ingresa el número de la opción que deseas para {materia} (1-{len(opciones_compatibles)}): ")
                if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones_compatibles):
                    mejor_opcion = opciones_compatibles[int(seleccion) - 1]
                    break
                print("❌ Entrada inválida. Intenta de nuevo.")

            for dia in normalizar_texto(mejor_opcion["DIA"]).split(","):
                horarios_ocupados.append({
                    "DIA": dia.strip(),
                    "INI": mejor_opcion["HORA_INICIO"],
                    "FIN": mejor_opcion["HORA_FIN"]
                })

            recomendadas.append({
                "ASIGNATURA": mejor_opcion["ASIGNATURA"],
                "GRUPO": mejor_opcion["GRUPO"],
                "DIA": mejor_opcion["DIA"],
                "HORA_INICIO": mejor_opcion["HORA_INICIO"],
                "HORA_FIN": mejor_opcion["HORA_FIN"],
                "AULA": mejor_opcion["AULA"],
                "DOCENTE": mejor_opcion["DOCENTE"],
                "NOTA": f"✅ Opción elegida entre {len(opciones_compatibles)} disponibles."
            })
        else:
            recomendadas.append({
                "ASIGNATURA": materia,
                "GRUPO": "NO COMPATIBLE",
                "DIA": "—",
                "HORA_INICIO": "—",
                "HORA_FIN": "—",
                "AULA": "—",
                "DOCENTE": "—",
                "NOTA": "⚠️ No se encontró horario compatible"
            })

    horario = pd.DataFrame(recomendadas)
    print("\n📋 Resultado de recomendación:\n")
    print(horario[["ASIGNATURA", "GRUPO", "DIA", "HORA_INICIO", "HORA_FIN", "NOTA"]])
    return horario, programa_norm

# === 4. VISUALIZADOR DE HORARIO ===

def visualizar_horario(horario_df, programa, contactos_df):
    contactos_df.columns = contactos_df.columns.str.upper().str.strip()
    horario_exp = horario_df.copy()
    horario_exp = horario_exp.assign(DIA=horario_exp["DIA"].str.split(",")).explode("DIA").reset_index(drop=True)
    horario_exp["DIA"] = horario_exp["DIA"].str.strip().str.upper()

    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_title("📒 Horario sugerido de materias", fontsize=14)

    dias_semana = {"LUN": 0, "MAR": 1, "MIE": 2, "JUE": 3, "VIE": 4, "SAB": 5}
    colores = ["#FFA07A", "#90EE90", "#87CEFA", "#D8BFD8", "#FFD700", "#CD5C5C"]

    for i, row in horario_exp.iterrows():
        if row["DIA"] in dias_semana and row["HORA_INICIO"] != "—":
            try:
                inicio = int(row["HORA_INICIO"].split(":")[0])
                fin = int(row["HORA_FIN"].split(":")[0])
                dia = dias_semana[row["DIA"]]
                ax.barh(
                    y=range(inicio, fin),
                    width=0.8,
                    left=dia,
                    height=1,
                    color=colores[i % len(colores)],
                    edgecolor="black",
                )
                ax.text(
                    dia + 0.05,
                    inicio + 0.5,
                    f"{row['ASIGNATURA']}\n({row['GRUPO']})",
                    va="center",
                    ha="left",
                    fontsize=9,
                    color="black",
                    wrap=True,
                )
            except:
                continue

    ax.set_yticks(range(6, 22))
    ax.set_yticklabels([f"{h}:00" for h in range(6, 22)])
    ax.set_xticks(range(6))
    ax.set_xticklabels(["LUN", "MAR", "MIE", "JUE", "VIE", "SAB"])
    ax.set_xlim(-0.5, 5.5)
    ax.invert_yaxis()
    for x in range(6):
        ax.axvline(x=x, color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

    plt.grid(True, axis="y", linestyle="--", alpha=0.3)

    no_ofertadas = horario_df[horario_df["NOTA"].str.contains("no se ofertó", case=False)]
    if not no_ofertadas.empty:
        lista_materias = ", ".join(no_ofertadas["ASIGNATURA"].tolist())
        row_contacto = contactos_df[contactos_df["PROGRAMA"] == programa.upper()]
        correo = row_contacto["CORREO"].values[0] if not row_contacto.empty else "facultad@usc.edu.co"
        pbx = row_contacto["PBX"].values[0] if "PBX" in row_contacto.columns and not row_contacto.empty else "(602) 5183000"
        mensaje = f"△ Las siguientes materias no fueron ofertadas: {lista_materias}.\n"
        mensaje += f"📩 Comunícate con la facultad al correo: {correo} | ☎ PBX: {pbx}"
        plt.figtext(0.5, -0.05, mensaje, wrap=True, ha='center', fontsize=10, color='red')

    plt.tight_layout()
    plt.show()

from horarios import recomendar_horarios, visualizar_horario

horario_sugerido, programa_estudiante = recomendar_horarios(pensum, materias_agrupadas)
visualizar_horario(horario_sugerido, programa_estudiante, contactos_df)
