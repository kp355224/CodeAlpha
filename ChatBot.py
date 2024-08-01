import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import random

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

responses = {
    "hello": ["Hello! How can I help you today?", "Hi there! What can I do for you?", "Hey! How's it going?"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "how are you": ["I'm just a bunch of code, but I'm here to help!", "I'm good! How can I assist you?", "Doing great! What about you?"],
    "default": ["I'm not sure I understand. Could you please elaborate?", "Sorry, I didn't get that. Can you rephrase?", "I'm here to help! Can you give me more details?"]
}

def preprocess_text(text):
    
    tokens = word_tokenize(text.lower())
    
    
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]
    
    
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    return " ".join(lemmatized_tokens)

def get_response(user_input):
    preprocessed_input = preprocess_text(user_input)
    
    for key in responses:
        if key in preprocessed_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

def chat():
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: " + random.choice(responses['bye']))
            break
        response = get_response(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    chat()
