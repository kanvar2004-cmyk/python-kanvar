# Simple Chatbot using while loop

print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()   # take input and convert to lowercase
    
    if user_input == "hi" or user_input == "hello":
        print("Chatbot: Hello! How are you?")
    elif user_input == "i am fine":
        print("Chatbot: That's great to hear!")
    elif user_input == "what is your name":
        print("Chatbot: I am your friendly chatbot 🤖")
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day!")
        break   # exit the loop
    else:
        print("Chatbot: Sorry, I don’t understand that.")