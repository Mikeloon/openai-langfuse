# remove: import openai
from dotenv import load_dotenv
load_dotenv()

from langfuse.openai import openai

# Basic LLM call to OpenAI using Responses API
response = openai.responses.create(
    input="Hello, world!",
    model="gpt-4.1-mini"
)

print(response.output_text)

