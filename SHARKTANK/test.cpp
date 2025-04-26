#include <iostream>
#include <iomanip>
#include <string>
#include <cctype>    // for toupper
using namespace std;

int main() {
    char cont = 'Y';
    while (toupper(cont) == 'Y') {
        // Print show banner
        cout << "\n****************** SASTA SHARK TANK ******************\n";
        
        // 1) Input Ask amount and Equity percentage
        double ask, equity;
        cout << "\nEnter the amount you are asking for (AskAmount): Rs ";
        cin >> ask;
        cout << "Enter the equity percentage you are offering (EquityPercent): ";
        cin >> equity;
        
        // Validate equity to avoid division by zero
        if (equity == 0) {
            cout << "Equity percentage cannot be zero. Try again.\n";
            continue;
        }
        
        // 2) Calculate the base valuation
        double valuation = (ask * 100.0) / equity;
        
        // Display pitch details
        cout << fixed << setprecision(2);
        cout << "\n------------------------------------------------------\n";
        cout << "Your Pitch Details:\n";
        cout << "------------------------------------------------------\n";
        cout << "Ask: Rs " << ask << " for " << equity << "% equity.\n";
        cout << "Company Valuation: Rs " << valuation << "\n";
        cout << "------------------------------------------------------\n\n";
        
        // 3) Calculate each shark's offer (money and equity)
        // Aman: 80% money, 150% equity
        double offerMoneyAman = ask * 0.8;
        double offerEqAman    = equity * 1.5;
        // Ashneer: 85% money, 140% equity
        double offerMoneyAshneer = ask * 0.85;
        double offerEqAshneer    = equity * 1.4;
        // Namita: 100% money, 100% equity (same as ask)
        double offerMoneyNamita = ask;
        double offerEqNamita    = equity;
        // Peyush: 110% money, 90% equity
        double offerMoneyPeyush = ask * 1.1;
        double offerEqPeyush    = equity * 0.9;
        // Anupam: 120% money, 80% equity
        double offerMoneyAnupam = ask * 1.2;
        double offerEqAnupam    = equity * 0.8;
        
        // 4) Display all shark offers in a stylized format
        cout << "Our Sharks have made their offers:\n";
        cout << "------------------------------------------------------\n";
        cout << "1. Aman    - Offers Rs " << offerMoneyAman 
             << " for " << offerEqAman << "% equity.\n";
        cout << "2. Ashneer - Offers Rs " << offerMoneyAshneer 
             << " for " << offerEqAshneer << "% equity.\n";
        cout << "3. Namita  - Offers Rs " << offerMoneyNamita 
             << " for " << offerEqNamita << "% equity.\n";
        cout << "4. Peyush  - Offers Rs " << offerMoneyPeyush 
             << " for " << offerEqPeyush << "% equity.\n";
        cout << "5. Anupam  - Offers Rs " << offerMoneyAnupam 
             << " for " << offerEqAnupam << "% equity.\n";
        cout << "------------------------------------------------------\n";
        
        // 5) User chooses which offer to accept
        int choice;
        cout << "Which offer do you choose? (Enter 1-5): ";
        cin >> choice;
        cout << "\n";
        
        string chosenName;
        double chosenMoney = 0, chosenEq = 0;
        bool validChoice = true;
        switch (choice) {
            case 1:
                chosenName = "Aman";
                chosenMoney = offerMoneyAman;
                chosenEq    = offerEqAman;
                break;
            case 2:
                chosenName = "Ashneer";
                chosenMoney = offerMoneyAshneer;
                chosenEq    = offerEqAshneer;
                break;
            case 3:
                chosenName = "Namita";
                chosenMoney = offerMoneyNamita;
                chosenEq    = offerEqNamita;
                break;
            case 4:
                chosenName = "Peyush";
                chosenMoney = offerMoneyPeyush;
                chosenEq    = offerEqPeyush;
                break;
            case 5:
                chosenName = "Anupam";
                chosenMoney = offerMoneyAnupam;
                chosenEq    = offerEqAnupam;
                break;
            default:
                validChoice = false;
                cout << "Invalid choice. No deal accepted.\n";
                break;
        }
        
        if (validChoice) {
            // 6) Confirm and display accepted offer
            cout << chosenName << "'s offer accepted!\n";
            cout << "You get Rs " << chosenMoney << " for " 
                 << chosenEq << "% equity from " << chosenName << ".\n";
            cout << "Congratulations on your deal!\n";
        }
        
        cout << "------------------------------------------------------\n";
        // Ask if the user wants to run another test
        cout << "Do you want to simulate another pitch? (Y/N): ";
        cin >> cont;
    }
    
    cout << "\nThank you for using Sasta Shark Tank Simulator!\n";
    return 0;
}