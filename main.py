import os
from dotenv import load_dotenv
from shark_ai import SharkTankAI

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Shark Tank Configuration
MIN_VALUATION = 1000
MAX_VALUATION = 100000000
MIN_EQUITY = 1
MAX_EQUITY = 100

# Ensure the API key is loaded
if not TOGETHER_API_KEY:
    raise ValueError("TOGETHER_API_KEY is not set in the environment variables.")

def validate_input(valuation: float, equity: float) -> bool:
    """
    Validates the valuation and equity input by the entrepreneur.
    """
    if not (MIN_VALUATION <= valuation <= MAX_VALUATION):
        print(f"Valuation must be between ${MIN_VALUATION:,} and ${MAX_VALUATION:,}")
        return False
    if not (MIN_EQUITY <= equity <= MAX_EQUITY):
        print(f"Equity must be between {MIN_EQUITY}% and {MAX_EQUITY}%")
        return False
    return True

def main():
    """
    Main function to simulate the Shark Tank negotiation process.
    """
    # Initialize the AI Shark with Together.ai API
    shark = SharkTankAI(TOGETHER_API_KEY)
    
    print("Welcome to AI Shark Tank!")
    print("=========================")
    
    while True:
        try:
            # Get pitch details from user
            pitch = input("\nWhat's your business idea? (or 'quit' to exit): ")
            if pitch.lower() == 'quit':
                print("Thank you for participating in AI Shark Tank!")
                break
                
            valuation = float(input("What's your company valuation? $"))
            equity = float(input("What percentage of equity are you offering? "))
            
            # Validate the input
            if not validate_input(valuation, equity):
                continue
            
            # Get shark's response
            response = shark.negotiate(pitch, valuation, equity)
            
            # Display the shark's response
            if response["interested"]:
                print("\nThe Shark is interested in your business!")
                print(f"Counter Offer: Valuation = ${response['counter_offer']['valuation']:,}, "
                      f"Equity = {response['counter_offer']['equity_asked']}%")
                print(f"Reasoning: {response['reasoning']}")
                print("Questions from the Shark:")
                for question in response["questions"]:
                    print(f"- {question}")
                print("Concerns from the Shark:")
                for concern in response["concerns"]:
                    print(f"- {concern}")
            else:
                print("\nThe Shark is not interested in your business.")
                print("Reason: The Shark believes the deal is not favorable.")
                
        except ValueError:
            print("Invalid input. Please enter numeric values for valuation and equity.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()