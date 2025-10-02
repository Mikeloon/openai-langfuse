
# Sistema Multi-Agente para Análisis de Ventas

Este proyecto implementa un sistema multi-agente modular utilizando el SDK de OpenAI Agents con un patrón orquestador-subagente para analizar datos de ventas.

## Estructura del Proyecto

```
├── config.py                  # Configuración base y utilidades comunes
├── data_lookup_agent.py      # Subagente de consulta de datos
├── data_analysis_agent.py    # Subagente de análisis de datos  
├── visualization_agent.py    # Subagente de visualización
├── orchestrator.py           # Agente orquestador principal
├── multi_agent_system.py     # Archivo principal del sistema
├── ejemplo_simple.py         # Ejemplo sin interacción del usuario
└── requirements.txt          # Dependencias del proyecto
```

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Configura tu clave de API de OpenAI:

**En Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="tu-clave-de-openai-aqui"
```

**En Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=tu-clave-de-openai-aqui
```

**En Linux/Mac:**
```bash
export OPENAI_API_KEY="tu-clave-de-openai-aqui"
```

## Uso

### Ejecución Interactiva
```bash
python multi_agent_system.py
```

### Ejemplo Simple (sin interacción)
```bash
python ejemplo_simple.py
```

## Arquitectura del Sistema

### Subagentes Especializados

1. **`data_lookup_agent.py`** - **Agente de Consulta de Datos**
   - Busca información en la base de datos de ventas
   - Genera consultas SQL automáticamente
   - Ejecuta consultas usando DuckDB

2. **`data_analysis_agent.py`** - **Agente de Análisis de Datos**
   - Analiza los datos recuperados
   - Extrae insights y patrones significativos
   - Genera análisis en formato markdown

3. **`visualization_agent.py`** - **Agente de Visualización**
   - Genera código Python para crear gráficos
   - Configura visualizaciones automáticamente
   - Utiliza matplotlib y otras librerías

4. **`orchestrator.py`** - **Orquestador Principal**
   - Coordina todos los subagentes
   - Maneja la comunicación con el usuario
   - Distribuye tareas según el contexto

### Archivos de Soporte

- **`config.py`**: Configuración centralizada, plantillas de prompts y utilidades
- **`multi_agent_system.py`**: Punto de entrada principal con interfaz interactiva
- **`ejemplo_simple.py`**: Demostración del sistema sin entrada del usuario

## Fuente de Datos

El sistema utiliza datos de ventas en formato Parquet:
- **Muestra (1000 filas)**: https://ikasten.io/data/sample.parquet
- **Dataset completo (697,894 filas)**: https://ikasten.io/data/Store_Sales_Price_Elasticity_Promotions_Data.parquet

## Ejemplos de Consultas

- "¿Cuáles son las 5 tiendas con mayor volumen de ventas?"
- "Analiza las ventas de la tienda 2420 comparándolas con la media"
- "Crea un gráfico de barras mostrando las ventas totales por tienda"
- "¿Cuál fue el producto más popular?"
- "Genera una visualización de la evolución de ventas por mes"

## Ventajas de la Arquitectura Modular

✅ **Mantenibilidad**: Cada agente está en su propio archivo
✅ **Escalabilidad**: Fácil agregar nuevos agentes o modificar existentes  
✅ **Reutilización**: Los agentes pueden usarse independientemente
✅ **Testing**: Cada componente puede probarse por separado
✅ **Colaboración**: Diferentes desarrolladores pueden trabajar en agentes distintos

## Requisitos

- Python 3.8+
- Clave de API válida de OpenAI
- Conexión a Internet para acceder a los datos de ventas