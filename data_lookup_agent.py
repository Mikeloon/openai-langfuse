#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subagente de Consulta de Datos

Este agente se encarga de buscar información en la base de datos de ventas
utilizando consultas SQL generadas automáticamente.
"""

import pandas as pd
import duckdb
from agents import Agent, function_tool
from config import TRANSACTION_DATA_FILE_PATH, generate_sql_query


@function_tool
async def lookup_sales_data(prompt: str) -> str:
    """Implementación de búsqueda de datos de ventas desde un archivo parquet usando SQL"""
    try:
        table_name = "sales"
        
        # Leer el archivo parquet en una tabla DuckDB
        df = pd.read_parquet(TRANSACTION_DATA_FILE_PATH)
        duckdb.sql(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM df")
        
        # Generar el código SQL
        sql_query = generate_sql_query(prompt, df.columns.tolist(), table_name)
        
        print(f"Ejecutando consulta SQL: {sql_query}")
        
        # Limpiar la respuesta para asegurarse de que solo incluye el código SQL
        sql_query = sql_query.strip()
        sql_query = sql_query.replace("```sql", "").replace("```", "")
        
        # Ejecutar la consulta SQL
        result = duckdb.sql(sql_query).df()
        
        return result.to_string()
    except Exception as e:
        return f"Error al acceder a los datos: {str(e)}"


def create_data_lookup_agent():
    """Crea y retorna el agente de consulta de datos"""
    return Agent(
        name="Agente de Consulta de Datos",
        model="gpt-4o-mini",
        instructions=(
            "Eres un agente que puede buscar información en una base de datos "
            "de ventas de una empresa para responder a las preguntas del usuario. Cuando tengas la información requerida, "
            "resúmela de manera clara y concisa. Asegúrate de responder a la pregunta con precisión "
            "y utiliza formato markdown cuando sea apropiado."
        ),
        tools=[lookup_sales_data],
    )


# Crear instancia del agente
data_lookup_agent = create_data_lookup_agent()