import os


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path= os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        target_is_file = os.path.isfile(target_file_path)
        target_is_python = target_file_path.endswith("py")

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not target_is_file:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        if not target_is_python:
            return f'Error: "{file_path}" is not a Python file'

        return "All good"
    
    except Exception as e:
        return f"Error: {e}"
