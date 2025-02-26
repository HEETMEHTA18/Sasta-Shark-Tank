#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    
    while(T--) {
        int A, B;
        cin >> A >> B;
        
        // Calculate company valuations
        // First investor: A dollars for 10%
        // Second investor: B dollars for 20%
        int valuation1 = A * 10; // Since A is for 10%, multiply by 10 to get full valuation
        int valuation2 = B * 5;  // Since B is for 20%, multiply by 5 to get full valuation
        
        if(valuation1 > valuation2) {
            cout << "FIRST" << endl;
        } else if(valuation2 > valuation1) {
            cout << "SECOND" << endl;
        } else {
            cout << "ANY" << endl;
        }
    }
    return 0;
} 