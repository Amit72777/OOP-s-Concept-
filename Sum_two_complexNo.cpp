// using class add tho complex number
#include <iostream>
using namespace std;
// create class
class complax
{
private:
    int r;
    int i; // decleare a private variable

public:
    complax() // default constructor
    {
        r = 0;
        i = 0;
    }
    complax(int m, int n) // constructor with parameter
    {
        r = m;
        i = n;
    }
    // Overloading the + operator for adding two complax numbers
    complax operator+(complax C)
    {
        // create a temporary complace object to store a class
        complax temp;
        // add real no. object attribute
        temp.r = r + C.r;
        // add imaginary no. atrribute in  object
        temp.i = r + C.i;

        return temp; // Return the resulting complax object
    }

    // show data
    void showdata()
    {
        cout << r << "+i" << i << endl;
    }
};

int main()
{
    // create a object
    complax c1(2, 3), c2(4, 6), c;

    // add to oject use constructor
    c = c1 + c2;

    // call member function
    c.showdata();

    return 0;
}