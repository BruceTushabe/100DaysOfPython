import nltk

from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer

#Dowlnlaod required NLTK data

nltk.download ('punkt')
nltk.download ('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Define chatbot patterns and responses
chatbot_pairs = [
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!", "Greetings!"]
    ],
    [
        r"what is your name?",
        ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]
    ],
    [
        r"how are you ?",
        ["I'm good, thanks! How about you?", "I'm doing well, thank you!"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me ChatBot.", "I'm ChatBot, nice to meet you!"]
    ],
    [
        r"(.*) (age|old) ?",
        ["I'm a chatbot, I don't have an age."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a chatbot, I exist in the digital world."]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by OpenAI using Python and NLTK."]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't quite understand that.", "Can you please rephrase that?"]
    ]
]


# Create a chat instance

chatbot = Chat(chatbot_pairs, reflections)

def generate_response(user_input):
    sentiment = sia.polarity_scores(user_input)["compound"]

    if sentiment > 0.3:
        response = "I am glad to hear that!"

    elif sentiment < -0.3:
        response = "I'm sorry to hear that. Is there anything I can do to help?"
    else:
        response = chatbot.respond(user_input)

    return response

# Start the chat 

print ("ChatBot: Hello, how can I assist you today? ")
while True:
    user_input = input("User: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye. Have a great day!")
        break

    else:
        try:

            response = generate_response(user_input)

        except Exception as e:
            print ("ChatBot: Oops! An error occured. Please try again.")

            continue
        print("ChatBot: ", response)

