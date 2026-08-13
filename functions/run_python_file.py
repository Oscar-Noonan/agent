import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
    

    if not abs_file_path.startswith(abs_working_directory + os.sep) and abs_file_path != abs_working_directory:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'

    try:
        command = ["python", abs_file_path]

        if args:
            command.extend(args)
        
        result = subprocess.run(
            command,
            cwd=abs_working_directory,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,
        )

        output_parts = []

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        
        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout.strip()}")
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr.strip()}")
                
        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"



schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python file and returns the output and errors if applicable.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The name of or path to the file to be run.",
                },
                "args": {
                    "type": "list of strings",
                    "description": "Any arguments you wish to add to the comand to run a python file.",
                },
            },
        },
    },
}