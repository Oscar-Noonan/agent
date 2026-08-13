import os


def get_file_content(working_directory: str, file_path: str) -> str:
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.join(abs_working_directory, file_path)
    

    if not abs_file_path.startswith(abs_working_directory):
        return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"
        
    if not os.path.isfile(abs_file_path):
        return f"Error: File not found or is not a regular file: '{file_path}'"
        

    try:
        with open(abs_file_path, "r", encoding="utf-8") as f:
            content = f.read(10000)
            if f.read(1):
                content += f"[...File '{file_path}' truncated at 10,000 characters]"
            return content
    except Exception as e:
        return f"Error: Could not read file '{file_path}': {str(e)}"