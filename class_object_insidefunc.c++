#include <iostream>
using namespace std;

class item
{
private:
    int x;
    int y;

public:
    void getdata(int m, int n)
    {
        x = m;
        y = n;
    }
    void putdata()
    {
        cout << "x = " << x << endl;
        cout << "y = " << y << endl;
    }
};

int main()
{
    item P, Q ;

    P.getdata(10, 20);


    P.putdata();

    return 0;
}