import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
try:
    api_key = os.environ.get("OPENROUTER_API_KEY")
except:
    raise Exception("environment variable not found")
