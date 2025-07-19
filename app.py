# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:02:17 2025

@author: Maria Almeida Pizarr
"""

import streamlit as st
from horarios import recomendar_horarios, visualizar_horario, cargar_datos as cargar_horarios
from tramites import asistente_tramites, cargar_datos as cargar_tramites

# Inicialización de estado
if "chat" not in st.session_state:
    st.session_state.chat = []
if "modo" not in st.session_state:
    st.session_state.modo = "inicio"
if "pensum" not in st.session_state:
    st.session_state.pensum, st.session_state.materias_agrupadas = cargar_horarios()
if "contactos_df" not in st.session_state:
    st.session_state.contactos_df = cargar_tramites()

# Encabezado
st.title("🎓 SANTI IA")
st.markdown("Asistente académico para recomendaciones de horarios y trámites universitarios.")

# Mostrar historial de chat
for rol, mensaje in st.session_state.chat:
    st.chat_message(rol).markdown(mensaje)

# Entrada del usuario
entrada = st.chat_input("Escribe aquí...")

if entrada:
    st.chat_message("usuario").markdown(entrada)
    st.session_state.chat.append(("usuario", entrada))

    # Detectar intención: horario o trámite
    if any(palabra in entrada.lower() for palabra in ["horario", "clases", "materias", "semestre"]):
        st.session_state.modo = "horario"
        pensum = st.session_state.pensum
        materias_agrupadas = st.session_state.materias_agrupadas
        contactos_df = st.session_state.contactos_df

        # Recomendación de horario
        horario, programa = recomendar_horarios(pensum, materias_agrupadas)
        st.session_state.chat.append(("santi", "Aquí tienes el horario que te recomiendo según tus preferencias:"))
        st.chat_message("santi").markdown("📚 Horario recomendado:")

        # Visualización en streamlit
        visualizar_horario(horario, programa, contactos_df)

    elif any(palabra in entrada.lower() for palabra in ["cancelación", "certificado", "paz", "retiro", "trámite"]):
        st.session_state.modo = "tramite"
        respuesta = asistente_tramites(entrada, st.session_state.contactos_df)
        st.session_state.chat.append(("santi", respuesta))
        st.chat_message("santi").markdown(respuesta)

    else:
        mensaje = "¿Quieres que te ayude con un horario o un trámite académico? 🧠"
        st.session_state.chat.append(("santi", mensaje))
        st.chat_message("santi").markdown(mensaje)
