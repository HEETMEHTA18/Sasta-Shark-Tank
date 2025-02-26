from shark_ai import SharkTankAI
from config import TOGETHER_API_KEY

def main():
    shark = SharkTankAI(TOGETHER_API_KEY)
    
    pitch = input("Enter your business idea pitch: ")
    valuation = input("Enter your company's valuation (in dollars): ")
    equity = input("Enter the percentage of equity offered: ")

    # Call the streaming negotiation method
    shark.stream_negotiate(pitch, valuation, equity)

if __name__ == "__main__":
    main()
