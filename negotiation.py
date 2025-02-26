import requests
import json
from config import TOGETHER_API_KEY

# Together AI API endpoint
API_URL = "https://api.together.xyz/v1/chat/completions"

def get_investor_response(conversation_history):
    """
    Send the conversation history to the Together AI API and return the investor's response.
    """
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-128K",
        "messages": conversation_history,
        "temperature": 0.7,
        "max_tokens": 1000
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} {response.text}"

def main():
    print("Welcome to AI Shark Tank Negotiation!")
    print("This simulation involves a negotiation between a Shark Tank investor and an entrepreneur pitching their company.\n")
    
    # Gather the entrepreneur's initial pitch details.
    pitch = input("Enter your business idea pitch: ")
    valuation = input("Enter your company's valuation (in dollars): ")
    equity = input("Enter the percentage of equity offered: ")
    
    # Initialize the conversation history.
    conversation = []
    
    # Add a system message to set the investor's role and tone.
    conversation.append({
        "role": "system",
        "content": (
            "You are a shrewd, critical, and experienced Shark Tank investor. "
            "Engage in a negotiation with the entrepreneur about their pitch, valuation, and equity offer. "
            "Challenge the valuation, ask tough questions, and argue about the terms. "
            "Keep your responses brief, direct, and argumentative."
        )
    })
    
    # Add the entrepreneur's initial pitch as a user message.
    conversation.append({
        "role": "user",
        "content": f"Pitch: {pitch}\nValuation: ${valuation}\nEquity Offered: {equity}%"
    })
    
    # Get and display the investor's first response.
    investor_reply = get_investor_response(conversation)
    print("\nInvestor:", investor_reply)
    conversation.append({"role": "assistant", "content": investor_reply})
    
    # Begin a negotiation loop where the entrepreneur can counter-argue.
    while True:
        entrepreneur_input = input("\nYour response (type 'exit' to end negotiation): ")
        if entrepreneur_input.lower() == "exit":
            print("Negotiation ended.")
            break
        # Append entrepreneur's counter-argument.
        conversation.append({"role": "user", "content": entrepreneur_input})
        # Get investor's next response.
        investor_reply = get_investor_response(conversation)
        print("\nInvestor:", investor_reply)
        conversation.append({"role": "assistant", "content": investor_reply})

if __name__ == "__main__":
    main()
