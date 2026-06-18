import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key and initialize client
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# --- Helper Functions ---

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    response = client.chat.completions.create(
        model="nex-agi/nex-n2-pro:free", 
        messages=messages,
    )
    return response.choices[0].message.content

# --- Main Chatbot Loop ---

def main():
    print("Welcome to the Chatbot! Type 'quit' or 'exit' to stop.\n")
    
    # Start with an empty message list
    messages = []
    
    # Repeat the process in a loop
    while True:
        # 1. Prompt the user to enter some input
        user_text = input("You: ")
        
        # Allow the user a way to exit the loop
        if user_text.lower() in ['quit', 'exit']:
            print("Ending chat. Goodbye!")
            break
            
        # 2. Add it to a list of messages
        add_user_message(messages, user_text)
        
        try:
            # 3. Call the API
            generated_text = chat(messages)
            
            # 4. Add generated text to the list of messages
            add_assistant_message(messages, generated_text)
            
            # 5. print the generated text
            print(f"Assistant: {generated_text}\n")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            # If API fails, remove the last user message so they can try again 
            # without duplicating their message in history
            if messages and messages[-1]['role'] == 'user':
                messages.pop()

if __name__ == "__main__":
    main()
