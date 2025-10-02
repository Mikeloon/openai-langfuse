from agents import Agent, Runner, SQLiteSession
import os
import asyncio
from dotenv import load_dotenv
import logfire
from langfuse import get_client

load_dotenv()

# Configure logfire instrumentation.
logfire.configure(
    service_name='my_agent_service',
    send_to_logfire=False,
)
# This method automatically patches the OpenAI Agents SDK to send logs via OTLP to Langfuse.
logfire.instrument_openai_agents()

langfuse = get_client()

# Verify connection
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")

from agents import set_tracing_export_api_key
set_tracing_export_api_key(os.getenv("OPENAI_API_KEY"))

async def main():
    # Create agent
    agent = Agent(
        name="Assistant",
        instructions="Responde de forma muy concisa y breve.",
    )

    # Create a session instance with a session ID
    session = SQLiteSession("conversation_123", "chat.db")

    # First turn
    result = await Runner.run(
        agent,
        "¿En qué ciudad está El Peine de los Vientos?",
        session=session
    )
    print(result.final_output)  # "Donostia"

    # Second turn - agent automatically remembers previous context
    result = await Runner.run(
        agent,
        "¿A qué provincia pertenece?",
        session=session
    )
    print(result.final_output)  # "Gipuzkoa"

    # Third turn - still remembers context
    result = await Runner.run(
        agent,
        "¿Cuál es la población de esa provincia?",
        session=session
    )
    print(result.final_output)  # "Aproximadamente 730.000 habitantes."
    
    # Flush traces to Langfuse
    langfuse.flush()
    print("Trazas enviadas a Langfuse.")

if __name__ == "__main__":
    asyncio.run(main())
