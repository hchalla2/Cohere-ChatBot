import cohere

# Set up the Cohere API key
cohere.api_key = "YOUR_COHERE_API_KEY"

def get_cohere_response(prompt):
    """
    Use Cohere's model to get a response based on the user's prompt.
    """
    response = cohere.generate("baseline-shrimp", prompt=prompt)
    return response.text

def chatbot():
    """
    Chatbot function to interact with the user.
    """
    print("Hello! I'm your chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_cohere_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
