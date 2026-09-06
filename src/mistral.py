import json
from config import Mistral_api_key
from mistralai.client import Mistral
from .tools import read_file, create_file, write_file_end, delete_file, create_directory,delete_directory,read_directory
from .memory import messages
from .tools_schema import Tools


model = "mistral-tiny"
client = Mistral(Mistral_api_key)


def chatMessage(message):
    messages.append({"role": "user", "content": message})

    chat_response = client.chat.complete(
            model = model,
            messages = messages,
            tools = Tools
        )

    message = chat_response.choices[0].message
    messages.append(message)

    if not message.tool_calls:
        return message.content

    for tool_call in message.tool_calls:
        args = json.loads(tool_call.function.arguments)

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
            case "read_directory":
                result = read_directory(**args)
            case "create_directory":
                result = create_directory(**args)
            case "delete_directory":
                result = delete_directory(**args)
            case _ :
                result = f"Tool '{tool_call.function.name}' is not implemented."

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )