#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subagente de Análisis de Datos

Este agente se encarga de analizar los datos de ventas para extraer
insights y patrones significativos.
"""

import os
from agents import Agent, function_tool
from openai import OpenAI
from config import DATA_ANALYSIS_PROMPT


@function_tool
async def analyze_sales_data(prompt: str, data: str) -> str:
    """Herramienta para el análisis de datos de ventas"""
    formatted_prompt = DATA_ANALYSIS_PROMPT.format(data=data, prompt=prompt)
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": formatted_prompt}],
    )
    
    analysis = response.choices[0].message.content
    return analysis if analysis else "No se pudo generar ningún análisis"


def create_data_analysis_agent():
    """Crea y retorna el agente de análisis de datos"""
    return Agent(
        name="Agente de Análisis de Datos",
        model="gpt-4o",
        instructions=(
            "Eres un agente de análisis de datos con acceso a herramientas de análisis. "
            "Los usuarios te harán preguntas sobre los datos de ventas y tú utilizarás "
            "las herramientas proporcionadas para analizar esos datos y responder "
            "a las preguntas. Asegúrate de proporcionar un análisis claro y preciso "
            "utilizando formato markdown."
        ),
        tools=[analyze_sales_data],
    )


# Crear instancia del agente
data_analysis_agent = create_data_analysis_agent()