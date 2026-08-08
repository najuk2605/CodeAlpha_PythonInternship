# Basic Rule-Based Chatbot

def chatbot_response(user_input):
    """Return a response based on the user's message."""

    message = user_input.lower().strip()

    if message == "hello" or message == "hi":
        return "Hi! Nice to meet you."

    elif message == "how are you":
        return "I'm fine, thanks! How are you?"

    elif message == "what is your name":
        return "I'm a simple Python chatbot."

    elif message == "what can you do":
        return "I can respond to a few basic messages."

    elif message == "bye" or message == "goodbye":
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that yet."


print("================================")
print("       PYTHON CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.\n")

while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower().strip() in ["bye", "goodbye"]:
        break