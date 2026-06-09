import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_parent_dirs = os.path.dirname(file_path)
        target_file_path= os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        target_is_dir = os.path.isdir(target_file_path)

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if target_is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        if file_path_parent_dirs:
            os.makedirs(file_path_parent_dirs, exist_ok=True)
        
        with open(target_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"
