
import os
import requests
from dotenv import load_dotenv

# Load API key and base URL from ~/.soonerai.env
load_dotenv(os.path.join(os.path.expanduser("~"), ".soonerai.env"))

API_KEY = os.getenv("SOONERAI_API_KEY")
BASE_URL = os.getenv("SOONERAI_BASE_URL", "https://ai.sooners.us").rstrip("/")
MODEL = os.getenv("SOONERAI_MODEL", "gemma3:4b")

if not API_KEY:
    raise RuntimeError("Missing SOONERAI_API_KEY in ~/.soonerai.env")

# Initialize conversation history with system message
history = [
    {
        "role": "system",
        "content": "You are SpongeBob SquarePants. Speak cheerfully and use ocean humor. Be enthusiastic and positive!"
    }
]

def call_api(messages):
    """Send messages to the API and return the assistant's reply."""
    url = f"{BASE_URL}/api/chat/completions"
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.7,
    }
    
    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=60,
        )
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            return f"Error {response.status_code}: {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

def main():
    """Main chat loop."""
    print("🧽 SpongeBob SquarePants Chatbot 🧽")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("\nSpongeBob: I'm ready! I'm ready! ...to say goodbye! See ya later!")
            break
        
        # Skip empty messages
        if not user_input:
            continue
        
        # Add user message to history
        history.append({"role": "user", "content": user_input})
        
        # Call API with full history
        reply = call_api(history)
        
        # Add assistant reply to history
        history.append({"role": "assistant", "content": reply})
        
        # Display SpongeBob's response
        print(f"\nSpongeBob: {reply}\n")

if __name__ == "__main__":
    main()