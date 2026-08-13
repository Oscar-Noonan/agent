import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI



try:
    parser = argparse.ArgumentParser(description="Agent")
    parser.add_argument("user_prompt", type=str, nargs="?", default="Oops looks like I forgot to input my prompt!", help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
except Exception as e:
    return f"Error: {e}"



load_dotenv()

try:
    api_key = os.environ.get("OPENROUTER_API_KEY")
except Exception as e:
    return f"Error: {e}"

try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
except Exception as e:
    return f"Error: {e}"



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
except Exception as e:
    return f"Error: {e}"

if args.verbose:
    print("User prompt: ", messages[0]["content"])

    print("Prompt tokens: ", response.usage.prompt_tokens)

    print("Response tokens: ", response.usage.completion_tokens)

print("Response: ", response.choices[0].message.content)    
