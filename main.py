import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI



try:
    parser = argparse.ArgumentParser(description="Agent")
    parser.add_argument("user_prompt", type=str, nargs="?", default="Oops looks like I forgot to input my prompt!", help="User prompt")
    args = parser.parse_args()
except:
    raise Exception("error parsing args")



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
        "content": args.user_prompt,
    }
]

try:
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages
    )
except:
    raise Exception ("error when calling openai client.chat.completions.create")

print("User prompt: ", messages[0]["content"])

print("Prompt tokens: ", response.usage.prompt_tokens)

print("Response tokens: ", response.usage.completion_tokens)

print("Response: ", response.choices[0].message.content)
