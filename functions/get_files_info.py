import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    if full_path is not os.path.abspath(working_directory):
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(full_path):
        raise Exception(f'Error: "{directory}" is not a directory')
    
    try:
        contents = os.listdir(full_path)
        dir_contents = ""
        for content in contents:
            file_size = os.path.getsize(os.path.join(full_path, content))
            is_dir = os.path.isdir(os.path.join(full_path, content))
            dir_contents += "".join(f"- {content}: file_size={file_size}, is_dir={is_dir}\n")
        return dir_contents.strip()
    
    except Exception as e:
        return f"Error: {e}"