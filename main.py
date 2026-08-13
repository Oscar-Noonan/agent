import os
import argparse
import json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions
from call_function import call_function



try:
    parser = argparse.ArgumentParser(description="Agent")
    parser.add_argument("user_prompt", type=str, nargs="?", default="Oops looks like I forgot to input my prompt!", help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
except Exception as e:
    raise f"Error: {e}"



load_dotenv()

try:
    api_key = os.environ.get("OPENROUTER_API_KEY")
except Exception as e:
    raise f"Error: {e}"

try:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
except Exception as e:
    raise f"Error: {e}"



messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user","content": args.user_prompt},
]

try:
    response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    tools=available_functions,
    )
except Exception as e:
    raise f"Error: {e}"

message = response.choices[0].message

if args.verbose:
    print("User prompt: ", messages[0]["content"])

    print("Prompt tokens: ", response.usage.prompt_tokens)

    print("Response tokens: ", response.usage.completion_tokens)

print("Response: ", message.content)

for tool_call in message.tool_calls:
    function_args = json.loads(tool_call.function.arguments or "{}")
    print(f"Calling function: {tool_call.function.name}({function_args})")
    result_message = call_function(tool_call, args.verbose)
