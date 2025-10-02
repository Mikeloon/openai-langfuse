#!/usr/bin/env python3
"""
Ejemplo simple del sistema multi-agente sin interacción del usuario
"""

import asyncio
from agents import Runner
from config import setup_openai_key
from orchestrator import orchestrator


async def run_example():
    """Ejecuta un ejemplo del sistema multi-agente"""
    
    # Configurar la API key
    setup_openai_key()
    
    # Consulta de ejemplo
    query = "¿Cuáles son las 5 tiendas con mayor volumen de ventas?"
    
    print("Sistema Multi-Agente para Análisis de Ventas")
    print("=" * 50)
    print(f"Consulta: {query}")
    print("Procesando...")
    print("-" * 50)
    
    try:
        result = await Runner.run(
            starting_agent=orchestrator,
            input=query
        )
        
        print("\nResultado:")
        print("=" * 50)
        print(result.final_output)
        
    except Exception as e:
        print(f"Error: {e}")
        print("Asegúrate de haber configurado OPENAI_API_KEY correctamente")


if __name__ == "__main__":
    asyncio.run(run_example())