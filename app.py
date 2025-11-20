# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# # Simple rule-based chatbot
# def chatbot_response(message):
#     message = message.lower()

#     # Greetings
#     if "hello" in message or "hi" in message:
#         return "Hello! How can I help you today?"

#     # Asking name
#     elif "your name" in message:
#         return "I'm ChatBot made using Flask 🙂"

#     # Asking how are you
#     elif "how are you" in message:
#         return "I'm doing great! Thanks for asking 😊"

#     # Joke
#     elif "joke" in message:
#         return "Why don't programmers like nature? Too many bugs! 🐞"

#     # About Python
#     elif "python" in message:
#         return "Python is a powerful and easy programming language!"

#     # About flask
#     elif "flask" in message:
#         return "Flask is a lightweight Python web framework."

#     # Bye
#     elif "bye" in message:
#         return "Goodbye! Have a nice day 😊"

#     # Default fallback
#     else:
#         return "Sorry, I didn't understand that. Try asking something else."


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/get", methods=["POST"])
# def get_bot_response():
#     user_message = request.form["message"]
#     response = chatbot_response(user_message)
#     return jsonify({"reply": response})


# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import random

# app = Flask(__name__)

# # Enhanced rule-based chatbot with more responses
# def chatbot_response(message):
#     message = message.lower()

#     # Greetings
#     if any(word in message for word in ["hello", "hi", "hey", "greetings"]):
#         responses = [
#             "Hello! How can I help you today?",
#             "Hi there! What can I do for you?",
#             "Hey! Nice to meet you 😊"
#         ]
#         return random.choice(responses)

#     # Asking name
#     elif "your name" in message or "who are you" in message:
#         return "I'm ChatBot, built with Flask! Nice to meet you 🙂"

#     # Asking how are you
#     elif "how are you" in message or "how r u" in message:
#         responses = [
#             "I'm doing great! Thanks for asking 😊",
#             "I'm functioning perfectly! How about you?",
#             "Great as always! I'm just code after all 🤖"
#         ]
#         return random.choice(responses)

#     # Jokes
#     elif "joke" in message or "funny" in message:
#         jokes = [
#             "Why don't programmers like nature? Too many bugs! 🐞",
#             "Why do Java developers wear glasses? Because they don't C#! 👓",
#             "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
#             "Why did the developer go broke? Because he used up all his cache! 💸"
#         ]
#         return random.choice(jokes)

#     # About Python
#     elif "python" in message:
#         return "Python is an amazing programming language! It's powerful, easy to learn, and has tons of libraries 🐍"

#     # About Flask
#     elif "flask" in message:
#         return "Flask is a lightweight and flexible Python web framework. Perfect for building web apps quickly! 🌐"

#     # Help
#     elif "help" in message or "what can you do" in message:
#         return "I can chat with you! Try asking me about Python, Flask, jokes, or just say hi! 💬"

#     # Time
#     elif "time" in message:
#         from datetime import datetime
#         current_time = datetime.now().strftime("%H:%M:%S")
#         return f"The current time is {current_time} ⏰"

#     # Date
#     elif "date" in message or "today" in message:
#         from datetime import datetime
#         current_date = datetime.now().strftime("%B %d, %Y")
#         return f"Today is {current_date} 📅"

#     # Thanks
#     elif "thank" in message:
#         return "You're welcome! Happy to help 😊"

#     # Bye
#     elif any(word in message for word in ["bye", "goodbye", "see you"]):
#         responses = [
#             "Goodbye! Have a nice day 😊",
#             "See you later! Take care! 👋",
#             "Bye! Come back anytime 🌟"
#         ]
#         return random.choice(responses)

#     # Default fallback
#     else:
#         responses = [
#             "Sorry, I didn't understand that. Try asking something else! 🤔",
#             "Hmm, I'm not sure about that. Can you rephrase?",
#             "I don't know how to respond to that yet. Try 'help' to see what I can do!"
#         ]
#         return random.choice(responses)


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/get", methods=["POST"])
# def get_bot_response():
#     user_message = request.form["message"]
#     response = chatbot_response(user_message)
#     return jsonify({"reply": response})


# if __name__ == "__main__":
#     app.run(debug=True)




from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Enhanced rule-based chatbot with personalized responses
def chatbot_response(message):
    message = message.lower()

    # Greetings
    if any(word in message for word in ["hello", "hi", "hey", "greetings"]):
        responses = [
            "Hello! I'm BuddyBot, here to chat with you!",
            "Hi there! What's on your mind today?",
            "Hey! Great to see you 😊"
        ]
        return random.choice(responses)

    # Asking name
    elif "your name" in message or "who are you" in message:
        return "I'm BuddyBot, your friendly Flask-powered assistant! 🤖"

    # Asking how are you
    elif "how are you" in message or "how r u" in message:
        responses = [
            "I'm doing great! Thanks for asking 😊",
            "Fantastic as always! How about you?",
            "Pretty good! I'm here and ready to chat 💬"
        ]
        return random.choice(responses)

    # Jokes
    elif "joke" in message or "funny" in message:
        jokes = [
            "Why don't programmers like nature? Too many bugs! 🐞",
            "Why do Java developers wear glasses? Because they don't C#! 👓",
            "What's a programmer's favorite hangout? The Foo Bar! 🍺",
            "Why did the developer quit? Because they didn't get arrays! 😄"
        ]
        return random.choice(jokes)

    # About Python
    elif "python" in message:
        return "Python is an awesome language! Easy to learn and super powerful 🐍"

    # About Flask
    elif "flask" in message:
        return "Flask is a lightweight Python web framework. Perfect for projects like this! 🌐"

    # Motivation
    elif "motivate" in message or "inspiration" in message:
        quotes = [
            "Believe you can and you're halfway there! 💪",
            "The only way to do great work is to love what you do! ❤️",
            "Code is like humor. When you have to explain it, it's bad! 😄",
            "Success is not final, failure is not fatal! Keep going! 🚀"
        ]
        return random.choice(quotes)

    # Help
    elif "help" in message or "what can you do" in message:
        return "I can chat, tell jokes, share motivational quotes, answer questions about Python/Flask, and more! Just ask away! 💬"

    # Time
    elif "time" in message:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time} ⏰"

    # Date
    elif "date" in message or "today" in message:
        from datetime import datetime
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"Today is {current_date} 📅"

    # Thanks
    elif "thank" in message:
        return "You're welcome! Happy to help 😊"

    # Bye
    elif any(word in message for word in ["bye", "goodbye", "see you", "later"]):
        responses = [
            "Goodbye! Have an amazing day 😊",
            "See you later! Take care! 👋",
            "Bye! Come chat anytime 🌟"
        ]
        return random.choice(responses)

    # Default fallback
    else:
        responses = [
            "Hmm, I'm not sure about that. Try asking something else! 🤔",
            "That's interesting! But I don't have an answer yet.",
            "I don't know how to respond to that. Type 'help' to see what I can do!"
        ]
        return random.choice(responses)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["message"]
    response = chatbot_response(user_message)
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)