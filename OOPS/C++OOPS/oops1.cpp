#include <iostream>

using namespace std;

class item
{
        int number;                     //private by default
        float cost;                     //private by default
    public:
        void getdata(int a, float b);   //prototype declaration
                                        //to be defined
        void putdata(void)
        {
            cout << "Number: " << number << "\n";
            cout << "Cost: " << cost << "\n";
        }
};

void item :: getdata(int a, float b)    // use membership label
{
        number = a;                     //private variables
        cost = b;                       //directly used
}

int main()
{
        item x;
        cout << "\nObject x " << "\n";

        x.getdata(100, 299.95);         //call member function
        x.putdata();                    //call member function

        return 0;
}