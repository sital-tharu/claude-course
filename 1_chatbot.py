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
        model="nex-agi/nex-n2-pro:free", # 1. Model updated here
        messages=messages,
        temperature=0.2, # Added temperature (lower = more precise, good for math)
    )
    return response.choices[0].message.content

# --- Main Chatbot Loop ---

print("Welcome to the Math Tutor Chatbot! Type 'quit' or 'exit' to stop.\n")

# 2. Add the System Prompt here! 
# Instead of an empty list, we start with the system instructions.
messages = [
    {"role": "system", "content": "You are an expert math tutor. You provide clear, step-by-step explanations for mathematical problems and encourage the student."}
]

# Repeat the process in a loop
while True:
    # Prompt the user to enter some input
    user_text = input("You: ")
    
    # Allow the user a way to exit the loop
    if user_text.lower() in ['quit', 'exit']:
        print("Ending chat. Goodbye!")
        break
        
    # Add it to a list of messages
    add_user_message(messages, user_text)
    
    try:
        # Call the API
        generated_text = chat(messages)
        
        # Add generated text to the list of messages
        add_assistant_message(messages, generated_text)
        
        # print the generated text
        print(f"\nMath Tutor: {generated_text}\n")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        # If API fails, remove the last user message so they can try again 
        if messages and messages[-1]['role'] == 'user':
            messages.pop()
