# Advanced Rule-Based Chatbot

print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! Nice to talk with you.")

    # Asking chatbot condition
    elif "how are you" in user:
        print("Bot: I am doing great. What about you?")

    # User feeling
    elif "fine" in user or "good" in user or "great" in user:
        print("Bot: That's wonderful!")

    elif "sad" in user or "bad" in user or "upset" in user:
        print("Bot: I hope things get better soon.")

    # Name questions
    elif "your name" in user:
        print("Bot: My name is AI Chatbot.")

    elif "my name" in user:
        print("Bot: Your name sounds nice!")

    # Creator
    elif "who made you" in user or "who created you" in user:
        print("Bot: Laiba created me using Python.")

    # Time questions
    elif "time" in user:
        print("Bot: Sorry, I cannot check real time right now.")

    # Study related
    elif "python" in user:
        print("Bot: Python is an easy and powerful programming language.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: AI means machines that can think and learn like humans.")

    elif "chatbot" in user:
        print("Bot: A chatbot is a program that talks with users.")

    # Personal questions
    elif "where are you from" in user:
        print("Bot: I live inside your computer.")

    elif "what can you do" in user:
        print("Bot: I can answer simple questions and chat with you.")

    # Thank you
    elif "thank" in user:
        print("Bot: You're welcome!")

    # Joke
    elif "joke" in user:
        print("Bot: Why did the computer go to school? To improve its bytes!")

    # Favorite color
    elif "favorite color" in user:
        print("Bot: My favorite color is blue.")

    # Food
    elif "food" in user or "eat" in user:
        print("Bot: Bots don't eat food, but pizza smells amazing!")

    # Weather
    elif "weather" in user:
        print("Bot: I hope the weather is nice today.")

    # Help
    elif "help" in user:
        print("Bot: You can ask me about Python, AI, chatbots, jokes, and more.")

    # Goodbye
    elif "bye" in user or "exit" in user or "quit" in user:
        print("Bot: Goodbye! Have a wonderful day.")
        break

    # Default answer
    else:
        print("Bot: That's interesting! Tell me more.")