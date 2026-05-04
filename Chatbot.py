#Rule Based AI Python ChatBot


import datetime
import time

name= input (" Welcome, enter your name : ") 
presentHour= datetime.datetime.now().hour

if presentHour <= 11:
    print("Good Morning, ", name)
elif 11 <= presentHour <= 17:
     print("Good Afternoon, ", name)
elif 17 <= presentHour <= 24:
    print("Good Evening, ", name)
else:
    print("Good Night, ", name)

print("Namaste! Welcome To Your ChatBot")
print("You can ask mr basic question, Type 'bye' to exit from the bot")

#Chatbot Memory Creation [ dictionary of responses ]

responses = {
    "hello" : "Hi, Welcome. How can I help you?",
    "how are you" : "I am very fine. Thank You!",
    "who are you?" : "I am a smart AI chatbot",
    "motivate me" : "Keep going. Every bug of your project makes you a better developer",
    "okay" : "Great 😊",
    "bye" : "GoodBye! 💕"
 }

#Method/Function to get response of ChatBOt

def GetResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower().strip()

    if userQuestion in responses:
        return responses[userQuestion]
    else:
        return "Oops! I am still learning and didn't quite get that"
    


# Take user input

while True:
    
    userInput= input("Please ask your question:")
    reply= GetResponseOfBot(userInput)
    print("Bot Responses :", reply)

    if "bye" in userInput.lower():
        break
