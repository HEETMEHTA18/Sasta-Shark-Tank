#include <iostream>
using namespace std;

int main() {
    int T;
    cout << "Welcome to Sasta Shark Tank!" << endl;
    cout << "Enter the number of test cases: ";
    cin >> T;  // Number of entrepreneurs (test cases)

    while (T--) {
        double askAmount;
        double equityPercent;
        cout << "--- Welcome to Sasta Shark Tank ---" << endl;
        cout << "Enter the amount you are asking for (Rupees:): ";
        cin >> askAmount;
        cout << "Enter the equity percentage you are offering (%): ";
        cin >> equityPercent;

        // Calculate the company's valuation
        double valuation = (askAmount * 100.0) / equityPercent;

        // Display the Shark's valuation
        cout << "Based on your ask, the Shark values your company at: Rupess:" << valuation << endl;
        cout<< "----------------------------------" << endl;        

        // Shark's decision (Simple logic)
        if (valuation >= 1000000) {
            cout << "Shark says: 'You have a Million Rupess Idea! I am IN!'" << endl;
        } else if (valuation >= 500000) {
            cout << "Shark says: 'Interesting... I will offer, but at a slightly higher equity!'" << endl;
        } else {
            cout << "Namita says: 'Too small for me. I am OUT!'" << endl;
        }

        cout << "----------------------------------" << endl;
    }

    return 0;
}
