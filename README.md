
# Sasta-Shark-Tank Simulator

**AI Shark Tank Simulator** is an interactive simulation where entrepreneurs pitch their business ideas and an AI-powered investor provides real-time feedback, counter-offers, and tough questions—just like on the TV show *Shark Tank*.

## Features

- **Interactive Pitch Simulation:**  
  Enter your business idea, company valuation, and equity offer to initiate a negotiation.

- **AI-Powered Investor:**  
  The investor's responses are generated using the Together AI API, providing realistic counter-offers, reasoning, questions, and concerns.

- **Modular Design:**  
  - **config.py:** Stores configuration settings and API key.
  - **main.py:** Entry point for the interactive simulation.
  - **shark_ai.py:** Contains the logic to interface with the Together AI API.
  - **negotiation.py:** (Optional) Supports a multi-turn negotiation simulation.
  - **together_ai_chat.py:** Demonstrates streaming API responses.
  - **shark_tank_calculator.cpp:** A C++ tool for basic valuation comparisons.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/HEETMEHTA18/Sasta-Shark-Tank.git
   cd Sasta-Shark-Tank
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the API Key:**
   Create a `.env` file in the project root with the following content:
   ```dotenv
   TOGETHER_API_KEY=your_api_key_here
   ```
   Ensure you add `.env` to your `.gitignore` to keep your API key secure.

4. **Run the Simulator:**
   ```bash
   python negotiations.py
   ```

## Project Structure

- **config.py:** Contains configuration settings and loads the API key from the `.env` file.
- **main.py:** The main interactive script where the entrepreneur enters their pitch.
- **shark_ai.py:** Interacts with the Together AI API to generate investor responses.
- **negotiation.py:** (Optional) Provides an extended negotiation with multiple rounds.
- **together_ai_chat.py:** Example script demonstrating streaming API responses.
- **shark_tank_calculator.cpp:** A C++ program for basic investor valuation comparisons.
- **requirements.txt:** Lists Python dependencies.
- **.env:** Stores sensitive environment variables (not committed to Git).

## Usage

Run the simulation by executing:

```bash
python negotiations.py
```

## Acknowledgements

- Powered by the Together AI API.
- Inspired by the negotiation style of *Shark Tank*.
