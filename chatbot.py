import tkinter as tk
import random

# ================= RESPONSES =================
responses = {
    "greetings": ["hello", "hi", "hey", "salam", "assalamualaikum"],
    "how_are_you": ["how are you", "kaisy ho", "kesa ho"],
    "bye": ["bye", "goodbye", "see you"],
    "name": ["your name", "who are you"],
    "thanks": ["thanks", "thank you", "shukriya"],
    "help": ["help", "what can you do"],
    "study": ["study", "exam", "assignment"],
    "weather": ["weather", "mosam"],
    "age": ["your age", "how old are you"],
    "creator": ["who made you", "your creator"],
}

bot_replies = {
    "greetings": ["Hello! 👋", "Hi there 😊", "Hey! How can I help you?"],
    "how_are_you": ["I'm doing great 😄", "All good! What about you?", "I'm fine, thanks!"],
    "bye": ["Goodbye! 👋", "Take care!", "See you later!"],
    "name": ["I am CodeAlpha Chatbot 🤖", "Your Python assistant!", "I'm your virtual helper!"],
    "thanks": ["You're welcome 😊", "No problem!", "Anytime!"],
    "help": ["I can chat with you, answer basic questions, and assist you!", "Try asking me anything 😊"],
    "study": ["Study hard and stay consistent 📚", "Don't worry, you will do great!", "Focus and keep practicing!"],
    "weather": ["I can't check live weather, but I hope it's nice outside ☀️"],
    "age": ["I am just a program, I don't have an age 😄"],
    "creator": ["I was created by a Python developer during internship 💻"],
    "default": ["Hmm... I didn't understand 🤔", "Can you rephrase that?", "Interesting! Tell me more!"]
}

# ================= RESPONSE FUNCTION =================
def get_response(user_input):
    user_input = user_input.lower()

    for key, words in responses.items():
        for word in words:
            if word in user_input:
                return random.choice(bot_replies[key])

    return random.choice(bot_replies["default"])

# ================= SEND FUNCTION =================
def send_message(event=None):
    user_text = entry.get()

    if user_text.strip() == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: " + user_text + "\n", "user")
    response = get_response(user_text)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

# ================= GUI =================
window = tk.Tk()
window.title("💬 Smart Chatbot")
window.geometry("520x600")
window.config(bg="#121212")

# Header
header = tk.Label(window, text="🤖 Smart AI Chatbot", bg="#1f1f2e",
                  fg="white", font=("Arial", 16, "bold"), pady=10)
header.pack(fill=tk.X)

# Chat frame
frame = tk.Frame(window, bg="#121212")
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_area = tk.Text(frame, height=22, width=55, bg="#1e1e2f", fg="white",
                    font=("Consolas", 12), wrap=tk.WORD, yscrollcommand=scrollbar.set,
                    bd=0)
chat_area.pack()

scrollbar.config(command=chat_area.yview)

# Styling tags
chat_area.tag_config("user", foreground="#00ffcc", font=("Arial", 11, "bold"))
chat_area.tag_config("bot", foreground="#ffcc00", font=("Arial", 11))

chat_area.config(state=tk.DISABLED)

# Input frame
input_frame = tk.Frame(window, bg="#121212")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=35, font=("Arial", 12), bd=2)
entry.grid(row=0, column=0, padx=10)

send_button = tk.Button(input_frame, text="Send",
                        command=send_message,
                        bg="#00adb5", fg="white",
                        font=("Arial", 10, "bold"), padx=10)
send_button.grid(row=0, column=1)

# Enter key binding
window.bind('<Return>', send_message)

# Welcome message
chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hello! I am your Smart Chatbot 🤖\nAsk me anything!\n\n", "bot")
chat_area.config(state=tk.DISABLED)

window.mainloop()