def chatbot_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Define responses based on predefined rules
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How can I help?"
    
    elif "your name" in user_input:
        return "I am a simple chatbot. I don't have a specific name, but you can call me Bot."
    
    elif "help" in user_input or "support" in user_input:
        return "I'm here to assist you with your queries. What do you need help with?"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a nice day!"
    
    else:
        return "Sorry, I didn't quite understand that. Can you rephrase it?"

# Main function to interact with the chatbot
def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Bot: {response}")

# Start the chatbot
if __name__ == "__main__":
    chat()
