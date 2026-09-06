import json
import os
from mistralai.client import Mistral
from config import Mistral_api_key

# .env file should contain the following line:
# MISTRAL_API_KEY=your_api_key_here
model = "mistral-tiny"

client = Mistral(Mistral_api_key)

# read the content of a file
# handle errors if the file does not exist or cannot be read
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

    


    
# write tool to read file and return its content
# so that the assistant can use it to answer questions about the file

Tools = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read the content of a file and return it as a string.",
            "parameters": {
                "type": "object",
                "properties": {
                   "path" : {"type": "string", "description": "The path to the file to read."},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "Create a new file with the given content.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "The path to the file to create."},
                    "content": {"type": "string", "description": "The content to write to the file."},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file_end",
            "description": "Append content to the end of a file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "The path to the file to write to."},
                    "content": {"type": "string", "description": "The content to append to the file."},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete_file",
            "description": "Delete a file at the given path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "The path to the file to delete."},
                },
                "required": ["path"],
            },
        },
    }
]

messages = [
]

tool_call_status = False
while True:
    if not tool_call_status:
        user_input = input("You: ")
        messages.append({"role": "user", "content": user_input})

    if user_input.lower() in ["exit", "quit"]:
        break


    chat_response = client.chat.complete(
        model = model,
        messages = messages,
        tools = Tools
    )

    message = chat_response.choices[0].message
    messages.append(message)

    if not message.tool_calls:
        print("Assistant:", message.content)
        tool_call_status = False
        continue

    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)
        print(f"Assistant is calling tool '{tool_call.function.name}' with arguments: {args}")

        result = None
        match tool_call.function.name:
            case "read_file":
                result = read_file(**args)
            case "create_file":
                result = create_file(**args)
            case "write_file_end":
                result = write_file_end(**args)
            case "delete_file":
                result = delete_file(**args)
            case _:
                result = f"Tool '{tool_call.function.name}' is not implemented."
            

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )

        tool_call_status = True
