#include <iostream>
using namespace std;

int main() {
    int T;
    cout << "Welcome to Sasta Shark Tank!" << endl;
    cin >> T;  // Number of test cases

    while (T--) {
        int A, B;
        cout<<"Enter the amount offered by the first investors: ";
        cin >> A;
        cout<<"Enter the amount offered by the second investors: ";
        cin>> B;

        // Calculate valuations
        int valuation_first = A * 10;
        int valuation_second = B * 5;

        // Print a fancy pitch
        cout << "--- Sasta Shark Tank Pitch ---" << endl;
        cout << "First Investor's Offer: $" << A << " for 10% Valuation: $" << valuation_first << endl;
        cout << "Second Investor's Offer: $" << B << " for 20% Valuation: $" << valuation_second << endl;

        // Final decision
        cout << "=> Decision: ";
        if (valuation_first > valuation_second) {
            cout << "FIRST" << endl;
        } else if (valuation_second > valuation_first) {
            cout << "SECOND" << endl;
        } else {
            cout << "ANY" << endl;
        }
        cout << "-------------------------------" << endl; // Stylish separator
    }

    return 0;
}