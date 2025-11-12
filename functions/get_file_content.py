import os
from functions.config import MAX_CHARS



def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: "{file_path}" is not a directory'
    
    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if f.read(MAX_CHARS) > 10000:
            file_content_string.append(f"[...File {file_path} truncated at 10000 characters]")