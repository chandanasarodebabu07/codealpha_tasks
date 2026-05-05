from chatbot import get_answer

print("Chatbot started! Type 'exit' to stop.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    print("Bot:", get_answer(user))