import requests
import json
from typing import Dict, Any

class SharkTankAI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.together.xyz/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def negotiate(self, pitch: str, valuation: float, equity_offered: float) -> Dict[str, Any]:
        # Create a prompt for the AI shark
        prompt = f"""
        You are a shrewd investor on Shark Tank. The entrepreneur has made the following pitch:
        
        Pitch: {pitch}
        Asked Valuation: ${valuation:,}
        Equity Offered: {equity_offered}%
        
        As an investor, analyze this deal and respond in the following JSON format:
        {{
            "interested": boolean,
            "counter_offer": {{
                "valuation": number,
                "equity_asked": number
            }},
            "reasoning": string,
            "questions": [string],
            "concerns": [string]
        }}
        """
        
        try:
           payload = {
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo-128K",
    "messages": [
        {"role": "system", "content": "You are an experienced Shark Tank investor."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7,
    "max_tokens": 1000
}

            
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            content = result.get('choices', [{}])[0].get('message', {}).get('content', '')
            
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # Fallback response if AI doesn't return valid JSON
                return {
                    "interested": False,
                    "counter_offer": {
                        "valuation": valuation * 0.8,
                        "equity_asked": min(equity_offered * 1.5, 100)
                    },
                    "reasoning": content,
                    "questions": ["Could you explain your business model?"],
                    "concerns": ["Response format was unclear"]
                }
                
        except Exception as e:
            return {"error": f"API Error: {str(e)}"} 