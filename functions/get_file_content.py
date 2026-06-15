import os

from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_file_path= os.path.normpath(os.path.join(working_directory_abs, file_path))
        valid_target_file = os.path.commonpath([working_directory_abs, target_file_path]) == working_directory_abs
        target_is_file = os.path.isfile(target_file_path)

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not target_is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file_path) as f:
            file_content =  f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{target_file_path}" truncated at {MAX_CHARS} characters]'

        return file_content
    
    except Exception as e:
        return f"Error: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Returns a string in a file specified by a file path relative to the working directory, truncated after {MAX_CHARS}.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path starting from the working directory that points to the file to be read"
            )
        },
        required=["file_path"]
    )
)