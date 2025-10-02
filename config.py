#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuración y utilidades base para el sistema multi-agente
"""

import os
from openai import OpenAI

# Configuración de datos
TRANSACTION_DATA_FILE_PATH = 'https://ikasten.io/data/sample.parquet'

# Plantillas de prompts
SQL_GENERATION_PROMPT = """
Genera una consulta SQL basada en el siguiente prompt. No respondas con nada más que la consulta SQL.
El prompt es: {prompt}

Las columnas disponibles son: {columns}
El nombre de la tabla es: {table_name}
"""

DATA_ANALYSIS_PROMPT = """
Analiza los siguientes datos: {data}
Tu trabajo es responder a la siguiente pregunta: {prompt}
"""

CHART_CONFIGURATION_PROMPT = """
Genera una configuración de gráfico basada en estos datos: {data}
El objetivo es mostrar: {visualization_goal}
"""

CREATE_CHART_PROMPT = """
Escribe código Python para crear un gráfico basado en la siguiente configuración.
Solo debes devolver el código Python, sin ningún otro texto explicativo.
config: {config}
"""

ORCHESTRATOR_PROMPT = (
    "Eres el orquestador de un sistema multi-agente. Tu tarea es tomar "
    "la consulta del usuario y pasarla al sub-agente/herramienta apropiado. Los sub-agentes "
    "verán la entrada que proporcionas y la utilizarán para obtener toda "
    "la información que necesitas para responder a la consulta del usuario. Es posible "
    "que necesites llamar a múltiples agentes para obtener toda la información que necesitas. "
    "No menciones ni llames la atención sobre el hecho de que este es un sistema multi-agente "
    "en tu conversación con el usuario. Ten en cuenta que eres un asistente de análisis de ventas para una empresa privada "
    "y si el usuario pregunta sobre información de la empresa "
    "o finanzas, debes utilizar nuestros datos internos en lugar de información pública."
)


def setup_openai_key():
    """Configura la clave de API de OpenAI desde variables de entorno"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: Variable de entorno OPENAI_API_KEY no encontrada.")
        print("Configúrala con: export OPENAI_API_KEY='tu-clave-aqui'")
        print("O en Windows: set OPENAI_API_KEY=tu-clave-aqui")
        exit(1)
    return api_key


def generate_sql_query(prompt: str, columns: list, table_name: str) -> str:
    """Genera una consulta SQL basada en un prompt"""
    formatted_prompt = SQL_GENERATION_PROMPT.format(prompt=prompt, columns=columns, table_name=table_name)
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": formatted_prompt}],
    )
    return response.choices[0].message.content


# Importaciones verificadas
def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    try:
        from agents import Agent, Runner, function_tool
        return True
    except ImportError:
        print("Error: No se pudo importar 'agents'. Asegúrate de instalar openai-agents:")
        print("pip install openai-agents")
        return False

    try:
        from openai import OpenAI
        return True
    except ImportError:
        print("Error: No se pudo importar 'openai'. Asegúrate de instalar openai:")
        print("pip install openai")
        return False