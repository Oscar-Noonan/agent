import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    # gets the absolute filepath of working_directory
    abs_working_directory = os.path.abspath(working_directory)

    # construct the full path to directory
    target_directory = os.path.normpath(os.path.join(abs_working_directory, directory))

    # check if target_directory is in abs_working_directory
    valid_target_directory = os.path.commonpath([abs_working_directory, target_directory]) == abs_working_directory

    result: str = f"Result for '{directory}' directory:"


    if not valid_target_directory:
        result += f'\n   Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return result

    if not os.path.exists(target_directory) or not os.path.isdir(target_directory):
        result += f'\n   Error: "{directory}" is not a directory'
        return result
    

    items = os.listdir(target_directory)

    for item in items:
        item_path = os.path.join(target_directory, item)
        result += f"\n    - {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}"
    
    return result