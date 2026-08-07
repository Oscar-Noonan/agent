import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
try:
    api_key = os.environ.get("OPENROUTER_API_KEY")
except:
    raise Exception("environment variable not found")

try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
except:
    raise Exception ("cannot connect to API provider")

messages = [
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]

response = client.chat.completions.create(
  model="openrouter/free",
  messages=messages
)

print(response.choices[0].message.content)
