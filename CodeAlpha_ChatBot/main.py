def chatbot():
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! 👋")
        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day! 👋")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")
chatbot()
//
