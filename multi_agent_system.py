#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema Multi-Agente para Análisis de Ventas
Archivo principal que coordina todos los componentes
"""

import asyncio
from agents import Runner
from config import setup_openai_key, check_dependencies
from orchestrator import orchestrator


async def main():
    """Función principal para ejecutar el sistema multi-agente"""
    
    # Verificar dependencias
    if not check_dependencies():
        return
    
    # Configurar la API key
    setup_openai_key()
    
    print("Sistema Multi-Agente para Análisis de Ventas")
    print("=" * 50)
    print("Agentes disponibles:")
    print("1. Consulta de Datos - Busca información en la BBDD de ventas")
    print("2. Análisis de Datos - Analiza datos para extraer insights")
    print("3. Visualización - Genera código para crear gráficos")
    print("="*50)
    
    # Ejemplo de consulta
    query = await asyncio.to_thread(input, "\nIntroduce tu consulta (o presiona Enter para usar ejemplo): ")
    if not query.strip():
        query = "¿Cuáles son las 5 tiendas con mayor volumen de ventas?"
        print(f"Usando consulta de ejemplo: {query}")
    
    print("\nProcesando consulta...\n")
    
    try:
        result = await Runner.run(
            starting_agent=orchestrator,
            input=query
        )
        print("Resultado:")
        print("-" * 30)
        print(result.final_output)
    except Exception as e:
        print(f"Error al procesar la consulta: {e}")


if __name__ == "__main__":
    asyncio.run(main())