#include <iostream>
using namespace std;

int main() {
    cout << "What is your name? ";
    string name;
    getline(cin, name);
    cout << "Hello, " << name << ", nice to meet you!" << endl;

}
