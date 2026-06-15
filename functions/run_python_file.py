import os
import subprocess

from google.genai import types


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
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not target_is_python:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file_path]
        if args:
            command.extend(args)

        result: subprocess.CompletedProcess = subprocess.run(command, capture_output=True, text=True, timeout=30)

        result_description = f"Process exited with code {result.returncode}."

        if result.stdout:
            result_description += f" STDOUT: {result.stdout}."
        elif result.stderr:
            result_description += f" STDERR: {result.stderr}."
        else:
            result_description += f" No output produced."

        return result_description
    
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python procedure given by the file located in the file path relative to the working directory with the args provided as inputs to the function",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path starting from the working directory that points to the file to be run with the provided arguments"
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Arguments necessary to run the python procedure given by the file located in the file path relative to the working directory",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Strings representing the arguments to the python procedure given by the file located in the file path relative to the working directory"
                )
            )
        },
        required=["file_path"]
    )
)