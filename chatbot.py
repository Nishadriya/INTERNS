import nltk
from nltk.chat.util import Chat, reflections

#define the chatbot responses
pairs = [
    ['hello|hi|hey',['hello!','hi there!','hey!']],
    ['how are you|how are you doing',["I'm doing well,thank you!","I'm fine, thanks!"]],
]

#Create the Chatbot
chatbot = Chat(pairs,reflections)

#Run the chatbot 
print("Chatbot:hi! how can I help you today?")
while True:
    user_input = input("You:")
    if user_input.lower() == 'exit':
        break
    response = chatbot.respond(user_input)
    print("Chatbot:",response)
