from src.mistral import chatMessage

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = chatMessage(user_input)
    print(f"AI: {response}")
