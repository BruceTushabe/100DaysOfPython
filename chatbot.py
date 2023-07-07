import nltk

#Dowlnlaod required NLTK data

nltk.download ('punkt')
nltk.download ('averaged_perceptron_tagger')
nltk.download ('wordnet')

#Define functions for processing user input and generating responses

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Tokenise user input

def tokenize(text):
    return word_tokenize(text.lower())

# Lemmatize words

def lemmatize(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

# Generate response

def generate_response (user_input):

    return "This is a simple response."

while True:

    user_input = input("User: ")
    tokens = tokenize(user_input)
    lemmas = lemmatize(tokens)
    response = generate_response(lemmas)

    if any(keyword in lemmas for keyword in [" Uganda", "Kampala", "africa"]):
        response = "Uganda is the greatest country in the world"
    print("Chatbot: " + response)



