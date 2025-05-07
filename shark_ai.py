class SharkTankAI:
    def __init__(self, api_key):
        self.api_key = api_key

    def negotiate(self, pitch, valuation, equity):
        # Simulate a response from the AI
        return {
            "interested": True,
            "counter_offer": {
                "valuation": valuation * 0.9,
                "equity_asked": equity + 5,
            },
            "reasoning": "We believe this valuation is more realistic.",
            "questions": ["What is your customer acquisition cost?", "What is your revenue growth rate?"],
            "concerns": ["Market competition is high.", "Your profit margins are low."],
        }