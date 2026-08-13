import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_directory, file_path)
    

    if not abs_file_path.startswith(abs_working_directory + os.sep) and abs_file_path != abs_working_directory:
        return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"
    
    if os.path.isdir(abs_file_path):
        return f"Error: '{file_path}' is a directory, cannot overwrite it with a file"


    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        return f"Error: Could not write to file '{file_path}': {str(e)}"

    return f"Successfully wrote to '{file_path}' ({len(content)} characters written)"