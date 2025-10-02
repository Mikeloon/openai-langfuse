#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subagente de Visualización de Datos

Este agente se encarga de generar código Python para crear
visualizaciones de los datos de ventas.
"""

import os
from pydantic import BaseModel, Field
from agents import Agent, function_tool
from openai import OpenAI
from config import CHART_CONFIGURATION_PROMPT, CREATE_CHART_PROMPT


class VisualizationConfig(BaseModel):
    """Configuración para la visualización de datos"""
    chart_type: str = Field(..., description="Tipo de gráfico a generar")
    x_axis: str = Field(..., description="Nombre de la columna del eje x")
    y_axis: str = Field(..., description="Nombre de la columna del eje y")
    title: str = Field(..., description="Título del gráfico")


def extract_chart_config(data: str, visualization_goal: str) -> dict:
    """Genera configuración de visualización de gráficos"""
    formatted_prompt = CHART_CONFIGURATION_PROMPT.format(data=data, visualization_goal=visualization_goal)
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": formatted_prompt}],
        response_format=VisualizationConfig,
    )
    
    try:
        content = response.choices[0].message.parsed
        return {
            "chart_type": content.chart_type,
            "x_axis": content.x_axis,
            "y_axis": content.y_axis,
            "title": content.title,
            "data": data
        }
    except Exception:
        return {
            "chart_type": "line",
            "x_axis": "date",
            "y_axis": "value",
            "title": visualization_goal,
            "data": data
        }


def create_chart(config: dict) -> str:
    """Crea un gráfico basado en la configuración de entrada"""
    formatted_prompt = CREATE_CHART_PROMPT.format(config=config)
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": formatted_prompt}],
    )
    
    code = response.choices[0].message.content
    code = code.replace("```python", "").replace("```", "")
    return code.strip()


@function_tool
async def generate_visualization(data: str, visualization_goal: str) -> str:
    """Genera una visualización basada en los datos y el objetivo"""
    config = extract_chart_config(data, visualization_goal)
    code = create_chart(config)
    return code


def create_visualization_agent():
    """Crea y retorna el agente de visualización"""
    return Agent(
        name="Agente de Visualización de Datos",
        model="gpt-4o",
        instructions=(
            "Eres un agente de visualización de datos con acceso a herramientas para crear "
            "visualizaciones. Se te dará un conjunto de datos y un objetivo, y tu trabajo "
            "es generar código Python para crear una visualización que cumpla con ese objetivo. "
            "Asegúrate de que el código sea claro, bien comentado y fácil de entender."
        ),
        tools=[generate_visualization],
    )


# Crear instancia del agente
visualization_agent = create_visualization_agent()