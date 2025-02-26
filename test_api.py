import os
from dotenv import load_dotenv
from together import Together

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
print("API Key:", api_key)

client = Together(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-128K",
        messages=[{"role": "user", "content": "Test message"}],
        max_tokens=100,
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=False  # Use non-streaming for simplicity
    )
    print("Response:", response)
except Exception as e:
    print("Error:", e)
