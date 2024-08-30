import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

# Define chatbot responses
def get_response(user_input):
    if 'hi' in user_input or 'hello' in user_input:
        return "Hi there! How can I assist you today?"
    elif 'how are you' in user_input:
        responses = ["I'm fine, thank you! How can I help you?", "Pretty good! What can I do for you?", "Feeling great! How about you?"]
        return random.choice(responses)
    elif 'what can you do' in user_input or 'what do you do' in user_input:
        return "I can chat with you, answer questions, and provide information. Try asking me something!"
    elif 'your name' in user_input:
        return "My name is ChatBot. What's yours?"
    elif 'weather' in user_input:
        return "I can't check the weather, but you can use a weather app for that!"
    elif 'tell me a joke' in user_input:
        jokes = ["Why don't scientists trust atoms? Because they make up everything!",
                 "Parallel lines have so much in common. It’s a shame they’ll never meet.",
                 "I told my wife she should embrace her mistakes. She gave me a hug."]
        return random.choice(jokes)
    elif 'how old are you' in user_input or 'your age' in user_input:
        return "I don't have an age. I'm just a friendly program!"
    else:
        unknown_responses = ["Sorry, I didn't catch that. Can you try again?", "I'm not sure what you mean. Could you clarify?", "Could you please rephrase your question?"]
        return random.choice(unknown_responses)

def send_message():
    user_input = entry.get().strip()
    if user_input:
        if user_input.lower() == 'bye':
            chat_window.config(state=tk.NORMAL)
            chat_window.insert(tk.END, "You: " + user_input + "\n")
            chat_window.insert(tk.END, "Bot: Goodbye! Have a great day!\n")
            chat_window.config(state=tk.DISABLED)
            entry.delete(0, tk.END)
            return

        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = get_response(user_input.lower())
        chat_window.insert(tk.END, "Bot: " + response + "\n")
        chat_window.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_window.yview(tk.END)

def clear_chat():
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)
    chat_window.config(state=tk.DISABLED)

def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Create the main window
root = tk.Tk()
root.title("ChatBot")

# Configure window appearance
root.geometry("600x500")
root.configure(bg="#e0f7fa")

# Create a chat window
chat_window = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, bg="#ffffff", fg="#000000", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry widget for user input
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=(10, 0), pady=10, fill=tk.X, expand=True)

# Create buttons
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

send_button = tk.Button(button_frame, text="Send", font=("Arial", 12), bg="#00796b", fg="white", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg="#d32f2f", fg="white", command=clear_chat)
clear_button.pack(side=tk.LEFT, padx=5)

# Add a personalized greeting
greeting = get_greeting()
chat_window.config(state=tk.NORMAL)
chat_window.insert(tk.END, "Bot: " + greeting + " How can I assist you today?\n")
chat_window.config(state=tk.DISABLED)

# Run the main loop
root.mainloop()
