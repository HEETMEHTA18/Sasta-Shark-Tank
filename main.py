from shark_ai import SharkTankAI
from config import TOGETHER_API_KEY, MIN_VALUATION, MAX_VALUATION, MIN_EQUITY, MAX_EQUITY

def validate_input(valuation: float, equity: float) -> bool:
    if not (MIN_VALUATION <= valuation <= MAX_VALUATION):
        print(f"Valuation must be between ${MIN_VALUATION:,} and ${MAX_VALUATION:,}")
        return False
    if not (MIN_EQUITY <= equity <= MAX_EQUITY):
        print(f"Equity must be between {MIN_EQUITY}% and {MAX_EQUITY}%")
        return False
    return True

def main():
    # Initialize the AI Shark with Together.ai API
    shark = SharkTankAI(TOGETHER_API_KEY)
    
    print("Welcome to AI Shark Tank!")
    print("=========================")
    
    while True:
        try:
            # Get pitch details from user
            pitch = input("\nWhat's your business idea? (or 'quit' to exit): ")
            if pitch.lower() == 'quit':
                break
                
            valuation = float(input("What's your company valuation? $"))
            equity = float(input("What percentage of equity are you offering? "))
            
            if not validate_input(valuation, equity):
                continue
            
            # Get shark's response
            response = shark.negotiate(pitch, valuation, equity)
            
            if "error" in response:
                print(f"Error: {response['error']}")
                continue
                
            print("\n=== Shark's Response ===")
            if response["interested"]:
                print("I'm interested in making a deal!")
            else:
                print("I'm out.")
                
            print(f"\nCounter Offer:")
            print(f"Valuation: ${response['counter_offer']['valuation']:,}")
            print(f"Equity Asked: {response['counter_offer']['equity_asked']}%")
            
            print(f"\nReasoning:")
            print(response["reasoning"])
            
            print("\nQuestions:")
            for q in response["questions"]:
                print(f"- {q}")
                
            print("\nConcerns:")
            for c in response["concerns"]:
                print(f"- {c}")
                
        except ValueError:
            print("Please enter valid numbers for valuation and equity.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 