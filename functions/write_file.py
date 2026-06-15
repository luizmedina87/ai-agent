import os

from google.genai import types


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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites the content of the file specified by the file path relative to the working directory with the content provided",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path starting from the working directory that points to the file to be overwritten with content"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content used to overwrite the file given by the file path"
            )
        },
        required=["file_path", "content"]
    )
)