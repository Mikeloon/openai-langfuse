#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orquestador del Sistema Multi-Agente

El orquestador coordina los diferentes subagentes y maneja la comunicación
con el usuario final.
"""

from datetime import datetime
from agents import Agent, function_tool
from config import ORCHESTRATOR_PROMPT
from data_lookup_agent import data_lookup_agent
from data_analysis_agent import data_analysis_agent
from visualization_agent import visualization_agent


@function_tool
def get_current_date():
    """Usa esta herramienta para obtener la fecha y hora actuales."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_orchestrator():
    """Crea y retorna el agente orquestador"""
    return Agent(
        name="Orquestador",
        model="gpt-4o",
        instructions=ORCHESTRATOR_PROMPT,
        tools=[
            data_lookup_agent.as_tool(
                tool_name="data_lookup_agent",
                tool_description="Buscar datos de ventas para obtener información actualizada"
            ),
            data_analysis_agent.as_tool(
                tool_name="data_analysis_agent",
                tool_description="Analizar datos de ventas para extraer insights"
            ),
            visualization_agent.as_tool(
                tool_name="visualization_agent",
                tool_description="Generar código para crear visualizaciones de datos"
            ),
            get_current_date,
        ],
    )


# Crear instancia del orquestador
orchestrator = create_orchestrator()