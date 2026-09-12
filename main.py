from src.memory import messages

from src.mistral import chatMessage

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    if user_input.strip() == "":
        continue

    if user_input.strip().lower() == "history":
        if not messages:
            print("No messages in history.")
        else:
            print("Message History:")
            print("----------------")
            for msg in messages:
                print(msg)
        continue
        

    response = chatMessage(user_input)
    print(f"AI: {response}")
