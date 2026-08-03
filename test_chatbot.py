from app.chatbot import SmartLibrarian

chatbot = SmartLibrarian()

response = chatbot.chat(
    "I want a fantasy book about friendship and magic."
)

print(response)