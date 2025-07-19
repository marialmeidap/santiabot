# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:01:22 2025

@author: Maria Almeida Pizarr
"""

def asistente_tramites():
    import pandas as pd

    contactos = pd.read_excel("/content/drive/MyDrive/Hackathon SantiBot/FACULTADES.xlsx")
    contactos.columns = contactos.columns.str.strip()
    contactos["PROGRAMA"] = contactos["PROGRAMA"].fillna("").astype(str).str.strip().str.upper()

    tramites = {
        "CANCELACIÓN DE MATERIA": [
            "📄 Paso 1: Verifica que estés dentro de las fechas del calendario académico.",
            "🖨️ Paso 2: Descarga el FORMATO DE MODIFICACIÓN DE MATRÍCULA 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA002_V10_FORMATO_MODIFICACION_MATRICULA_ACADEMICA.pdf",
            "✍🏼 Paso 3: Diligencia el formulario con tu información personal.",
            "🏫 Paso 4: Una vez diligenciado el formato, se debe remitir al CORREO_FACULTAD o entregarlo presencialmente.",
            "✅ Paso 5: Verifica en SINU que la solicitud haya sido tramitada y espera confirmación vía correo institucional."
        ],
        "SOLICITAR UN CERTIFICADO ACADEMICO": [
        "📺 Paso 1: Visualiza el video instructivo 👉 youtube.com/watch?v=xorYqJSlHpI",
        "💰 Paso 2: Consulta el valor del certificado 👉 https://www.usc.edu.co/index.php/servicios-financieros/liquidacion-y-actualizacion-de-recibos-5/derechos-pecuniarios",
        "🏦 Paso 3: Realiza el pago Mediante PSE o directamente en el banco (según el recibo)",
        "📧 Paso 4: Envía la solicitud al correo👉 certificados.academicos@usc.edu.co",
        "Adjunta: Comprobante de pago Nombre completoNúmero de identificación Tipo de certificado Periodo académico",
        "📩 Paso 5: Recibe el certificado por correo electrónico (en el plazo definido por la universidad)",
        "📘 Consulta tipos de certificados según tu condición: Estudiante, Egresado o Inactivo 👉 https://www.google.com/url?q=https%3A%2F%2Fwww.usc.edu.co%2Findex.php%2Fcertificaciones&sa=D&sntz=1&usg=AOvVaw3qhM5TaQ5KxZHF64lJiM5f"
    ],
    "MATRÍCULA ACADÉMICA ORDINARIA": [
        "📅 Paso 1: Consulta las fechas establecidas para la matrícula 👉 www.usc.edu.co/index.php/academico/calendario-academico",
        "💳 Paso 2: Verifica que tengas el pago financiero realizado.",
        "🖥️ Paso 3: Ingresa al Sistema de Información Académico SINUGWT y selecciona los cursos (materias) a matricular. 👉 http://www.google.com/url?q=http%3A%2F%2Fsinu.usc.edu.co%3A9191%2Fsinugwt%2F&sa=D&sntz=1&usg=AOvVaw1I-Ee1mNqFLqMp5WzIQ2jv",
        "📧 Paso 4: Si eres estudiante de primer semestre y no tienes usuario o contraseña de SINU, escribe a 👉 gestiontecnologica@usc.edu.co",
        "📘 Paso 5: Consulta el instructivo para realizar tu matrícula desde casa 👉 https://youtu.be/4uLLiqT8PR8",
        "🚫 Paso 6: No cierres tu matrícula, ya que esto impide realizar cambios de cursos o grupos.",
        "📩 Paso 7: Asegúrate de tener activo tu correo institucional. Si no lo tienes, solicítalo 👉 https://www.google.com/url?q=https%3A%2F%2Fencuestasipac.usc.edu.co%2Fsolicitud-correo&sa=D&sntz=1&usg=AOvVaw1peekz4sC5wNXfZAUDcAte"
    ],
    "MATRÍCULA ACADÉMICA EXTRAORDINARIA": [
        "📅 Paso 1: Consulta las fechas establecidas para la matrícula extraordinaria 👉 www.usc.edu.co/index.php/academico/calendario-academico",
        "💳 Paso 2: Realiza el pago de la matrícula financiera.",
        "📄 Paso 3: Descarga el Formato de Matrícula Académica Extraordinaria desde la web oficial de la USC.👉https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA001_V12_FORMATO_MATRCULA_ACADMICA_EXTRAORDINARIA-12.pdf",
        "✍️ Paso 4: Diligencia el formato con cuidado y firma en el espacio correspondiente (FIRMA ESTUDIANTE).",
        "📘 Paso 5: Consulta la guía para diligenciar correctamente formatos PDF 👉 ¿Cómo diligenciar los formatos ON-LINE? https://drive.google.com/file/d/1HgKP2wcsDQYVBWs6pWC1iM751NCTKH45/view?usp=sharing",
        "📧 Paso 6: Envía el formato diligenciado al CORREO_FACULTAD o entregarlo presencialmente en tú facultad."
    ],
    "CAMBIO DE GRUPO Y/O CAMBIO DE CURSO": [
        "🔄 Paso 1: Identifica el tipo de cambio que necesitas realizar:",
        "📘 Cambio de Grupo: Aplica cuando hay cruce de horario, pero se mantiene la misma asignatura.",
        "📗 Cambio de Curso: Aplica cuando deseas cambiar una asignatura por otra diferente.",
        "📄 Paso 2: Solicita y diligencia el formulario correspondiente según el tipo de cambio.👉https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA002_V10_FORMATO_MODIFICACION_MATRICULA_ACADEMICA.pdf",
        "📧 Paso 3: Envía el formulario al CORREO_FACULTAD o entregarlo presencialmente en tú facultad.",
        "📌 Paso 4: Espera la confirmación oficial del cambio solicitado."
    ],
    "RECIBO DE PAGO PARA MATRÍCULA PARCIAL O POR RANGO DE CRÉDITOS": [
        "📅 Paso 1: Consulta las fechas establecidas en el 👉 www.usc.edu.co/index.php/academico/calendario-academico para matrícula ordinaria o extraordinaria parcial.",
        "📄 Paso 2: Descarga el formato 'R-GA005_V5 FORMATO SOLICITUD LIQUIDACIÓN DE RECIBO MATRÍCULA PARCIAL' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA005_V8_FORMATO_SOLICITUD_LIQUIDACION_DE_RECIBO_MATRCULA_PARCIAL.pdf",
        "📝 Paso 3: Diligencia cuidadosamente el formato teniendo en cuenta el pensum de tu programa (Nuevo o Antiguo Pensum).",
        "✍🏼 Paso 4: Firma en los recuadros correspondientes: FIRMA ESTUDIANTE y RECIBÍ RESPUESTA - FIRMA ESTUDIANTE.",
        "💻 Paso 5: La solicitud puede realizarse vía electrónica, la Secretaría Académica te enviará el enlace para diligenciar el requerimiento.",
        "📧 Paso 6: Recibe la respuesta por correo electrónico o de forma presencial.",
        "⚠️ Nota: La universidad no genera devoluciones por concepto de matrículas parciales."
    ],
    "ADICIONAR CRÉDITOS": [
        "📅 Paso 1: Verifica que te encuentres dentro de las fechas establecidas en el 👉 Calendario Académico https://www.google.com/url?q=https%3A%2F%2Fwww.usc.edu.co%2Findex.php%2Facademico%2Fcalendario-academico&sa=D&sntz=1&usg=AOvVaw06-OodDVTw1P-jkn1s6z2y",
        "📚 Paso 3: Realiza tu matrícula académica completa y define tus horarios.",
        "✅ Paso 4: Cierra la matrícula académica desde el sistema.",
        "📄 Paso 5: Descarga y diligencia el 'Formato de Modificación de Matrícula' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA002_V10_FORMATO_MODIFICACION_MATRICULA_ACADEMICA.pdf",
        "📝 Paso 6: Firma en el campo correspondiente (FIRMA ESTUDIANTE) y asegúrate de diligenciar todo correctamente.",
        "📧 Paso 7: Envía el formato al CORREO_FACULTAD o entregarlo presencialmente en tú facultad.",
        "⚠️ Paso 8: Una vez adicionados los cursos, no podrás realizar cambios en la matrícula académica."
    ],
    "CANCELACIÓN Y/O APLAZAMIENTO DE SEMESTRE": [
        "📅 Paso 1: Asegúrate de estar dentro del plazo definido en el 👉 Calendario Académico. https://www.google.com/url?q=https%3A%2F%2Fwww.usc.edu.co%2Findex.php%2Facademico%2Fcalendario-academico&sa=D&sntz=1&usg=AOvVaw06-OodDVTw1P-jkn1s6z2y",
        "📄 Paso 2: Descarga el 'Formato de Cancelación de Semestre' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA004_V7_FORMATO_DE_CANCELACION_DE_SEMESTRE.pdf",
        "📝 Paso 3: Elabora una carta explicando las razones de tu cancelación.",
        "💳 Paso 4: Adjunta el recibo de pago de matrícula.",
        "🆔 Paso 5: Incluye fotocopia de tu documento de identidad ampliado al 150%.",
        "📧 Paso 6: Envía todos los documentos al CORREO_FACULTAD o entregarlo presencialmente en tú facultad.",
        "📌 Paso 7: Si la solicitud se realiza fuera del plazo, la Secretaría gestionará tu caso con las áreas competentes. Recibirás respuesta por correo."
    ],
    "SOLICITAR SALDO A FAVOR": [
        "📄 Paso 1: Reúne los siguientes documentos:",
        "✅ Fotocopia del recibo de pago.",
        "✅ Fotocopia del documento de identidad.",
        "✅ Carta dirigida a la Secretaría Académica, explicando los motivos de tu solicitud.",
        "📧 Paso 2: Envía la documentación al correo de la Secretaría Académica de tu Facultad o entrégala presencialmente.",
        "⚠️ Paso 3: Ten en cuenta que no se generan devoluciones por matrícula parcial o por rango de créditos.",
        "📘 Paso 4: Consulta la Resolución de Rectoría N°117 del 23 de noviembre de 2017, artículo 8 para más detalles."
    ],
    "SOLICITAR UN SUPLETORIO": [
        "📄 Paso 1: Descarga y diligencia el formato 'R-GA003 – Solicitud Pruebas y Exámenes' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA003_V9_FORMATO_SOLICITUD_PRUEBAS_Y_EXAMENES.pdf",
        "📝 Paso 2: Redacta una carta explicando el motivo por el cual no presentaste el examen, adjunta los soportes correspondientes (ej. incapacidad, constancia laboral, etc.).",
        "📧 Paso 3: Envía el formato y la carta al correo de tu Secretaría Académica o entrégalos presencialmente.",
        "🧑‍🏫 Paso 4: Contacta al docente responsable para coordinar la aplicación del supletorio.",
        "💵 Paso 5: Ten en cuenta que el examen supletorio tiene un costo según los Derechos Pecuniarios USC."
    ],
    "SOLICITAR UNA HABILITACIÓN": [
        "📄 Paso 1: Descarga y diligencia el formato 'R-GA003 – Solicitud Pruebas y Exámenes' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA003_V9_FORMATO_SOLICITUD_PRUEBAS_Y_EXAMENES.pdf",
        "📊 Paso 2: Verifica que tu nota definitiva esté entre 2.0 y 2.94 (Art. 48 Reglamento Estudiantil)",
        "📧 Paso 3: Envía el formato al correo de tu Secretaría Académica o entrégalo de forma presencial.",
        "💳 Paso 4: Realiza el pago correspondiente según los Derechos Pecuniarios USC.",
        "👩‍🏫 Paso 5: Contacta a tu docente para acordar la fecha y condiciones de la habilitación."
    ],
    "SOLICITAR PRUEBAS DE VALIDACIÓN": [
        "📄 Paso 1: Descarga y diligencia el formato 'R-GA003 – Solicitud Pruebas y Exámenes' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA003_V9_FORMATO_SOLICITUD_PRUEBAS_Y_EXAMENES.pdf",
        "📧 Paso 2: Envía el formato al CORREO_FACULTAD o entregarlo presencialmente en tú facultad.",
        "📩 Paso 3: Espera la notificación de aprobación por correo electrónico (previa aprobación del Consejo de Facultad).",
        "💳 Paso 4: Si es aprobada tu solicitud, descarga el recibo de pago y realiza el pago correspondiente.",
        "📑 Paso 5: Radica copia del comprobante de pago en la Secretaría Académica.",
        "👩‍🏫 Paso 6: La Secretaría notificará al docente y al estudiante para la aplicación de la prueba."
    ],
    "SOLICITAR PRUEBAS DE PROFICIENCIA": [
        "📄 Paso 1: Descarga y diligencia el formato 'R-GA003 – Solicitud Pruebas y Exámenes' 👉 https://www.usc.edu.co/wp-content/uploads/2023/09/R-GA003_V9_FORMATO_SOLICITUD_PRUEBAS_Y_EXAMENES.pdf",
        "📧 Paso 2: Envía el formato al CORREO_FACULTAD o entregarlo presencialmente en tú facultad.",
        "📩 Paso 3: Espera la notificación de aprobación por correo electrónico.",
        "💳 Paso 4: Si es aprobada tu solicitud, descarga el recibo de pago y realiza el pago. 👉 https://www.google.com/url?q=https%3A%2F%2Fapps.usc.edu.co%2F&sa=D&sntz=1&usg=AOvVaw2TH7Cccfe5q0PkNt17WjSa",
        "📑 Paso 5: Radica copia del comprobante en la Secretaría Académica.",
        "👩‍🏫 Paso 6: La Secretaría notificará al docente y al estudiante para realizar la prueba."
]

}


    tramites_con_carrera = [
        "CANCELACIÓN DE MATERIA",
        "SOLICITAR AMPLIACIÓN DE CUPO",
        "SOLICITAR PRUEBAS DE PROFICIENCIA",
        "SOLICITAR PRUEBAS DE VALIDACIÓN",
        "SOLICITAR UNA HABILITACIÓN",
        "SOLICITAR UN SUPLETORIO",
        "CANCELACIÓN Y/O APLAZAMIENTO DE SEMESTRE",
        "ADICIONAR CRÉDITOS",
        "CAMBIO DE GRUPO Y/O CAMBIO DE CURSO",
        "MATRÍCULA ACADÉMICA EXTRAORDINARIA"
    ]

    def personalizar_pasos(pasos, correo):
        return [paso.replace("CORREO_FACULTAD", correo) for paso in pasos]

    print("\n🤖 Bienvenido a *SANTI*, tu asistente académico inteligente.")

    while True:
        print("\n¿Qué trámite deseas realizar?")
        for i, t in enumerate(tramites, 1):
            print(f"{i}. {t}")
        print("0. Salir")

        try:
            opcion = int(input("\n🔢 Ingresa el número de tu opción: "))
        except ValueError:
            print("⚠️ Por favor ingresa un número válido.")
            continue

        if opcion == 0:
            print("👋 ¡Hasta pronto! SANTI siempre estará para ayudarte.")
            break
        elif 1 <= opcion <= len(tramites):
            nombre_tramite = list(tramites.keys())[opcion - 1]
            nombre = nombre_tramite.upper()
            if nombre in tramites:
                if nombre in tramites_con_carrera:
                    carrera = input("\n🎓 Ingresa tu carrera o programa: ").strip().upper()
                    coincidencias = contactos[contactos["PROGRAMA"].str.contains(carrera, case=False)]
                    if not coincidencias.empty:
                        correo = coincidencias["CORREO"].values[0]
                        pasos = personalizar_pasos(tramites[nombre], correo)
                        print(f"\n📌 Trámite: {nombre}")
                        for paso in pasos:
                            print(paso)
                    else:
                        print("⚠️ No se encontró el contacto de tu carrera. Intenta escribir el nombre completo.")
                else:
                    print(f"\n📌 Trámite: {nombre}")
                    for paso in tramites[nombre]:
                        print(paso)
        else:
            print("❌ Esa opción no existe. Intenta nuevamente.")
asistente_tramites()

