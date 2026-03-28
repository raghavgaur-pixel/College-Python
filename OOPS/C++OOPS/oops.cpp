#include <iostream>

using namespace std;
class person
{
    char name[30];
    int age;

    public:  // Access specifier mode
        void getdata(void); // Member Function
        void display(void); // Member Function
};
// Function Definition
void person :: getdata(void) // Scope Resolution Operator
{
        cout << "Enter Name: ";
        cin >> name;
        cout << "Enter Age: ";
        cin >> age;
}
// Function Definition
void person :: display(void)
{
    cout << "\nName: " << name;
    cout << "\nAge: " <<age;
}

int main()
{
    person p;
    p.getdata();
    p.display();

    return 0;
}
