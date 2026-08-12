import os

def get_files_info(working_dir: str, dir: str = ".") -> str:
    # gets the absolute filepath of working_dir
    abs_working_dir = os.path.abspath(working_dir)

    # construct the full path to dir
    target_dir = os.path.normpath(os.path.join(abs_working_dir, dir))

    # check if target_dir is in abs_working_dir
    valid_target_dir = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir

    if not valid_target_dir:
        return f'Error: Cannot list "{dir}" as it is outside the permitted working directory'
    elif not os.path.isdir(dir):
        return f'Error: "{dir}" is not a directory'
    else:
        return f'Success: "{dir}" is within the working directory'