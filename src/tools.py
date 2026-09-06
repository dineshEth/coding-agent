def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            # close file after reading
            content = f.read()
        return content
    except FileNotFoundError:
        return f"The file '{path}' does not exist."

def create_file(path, content):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"File '{path}' created successfully."
    except Exception as e:
        return f"Error creating file '{path}': {str(e)}"

def write_file_end(path, content):
    try:
        with open(path, "a", encoding="utf-8") as f:
            f.write(content)
        return f"Content appended to file '{path}' successfully."
    except Exception as e:
        return f"Error appending to file '{path}': {str(e)}"

def delete_file(path):
    try:
        os.remove(path)
        return f"File '{path}' deleted successfully."
    except FileNotFoundError:
        return f"The file '{path}' does not exist."
    except Exception as e:
        return f"Error deleting file '{path}': {str(e)}"
