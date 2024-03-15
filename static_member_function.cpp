#include <iostream>
using namespace std;

class item
{
private:
    int x;
    int y;
    static int m; // create a static variable
public:
    void getdata();
    void putdata();
    static int getcount(); // delcear a static function
};

// define a class member function outside a class 
void item ::getdata()
{
    cout << "Enter two number : " << endl;
    cin >> x >> y;
    m++;
}

int item ::m;  //  static variable  declare  globally 
void item ::putdata()
{
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
}

int item ::getcount()
{
    cout << "The No. of object is : " << m << endl;
}

int main()
{
    item P, Q;

    // call public member function in class 
    P.getdata();
    Q.getdata(); 

    P.putdata();
    Q.putdata();

    item ::getcount();  // call static function 

    return 0;
}

/*
Output :- 
Enter two number : 
10
50
Enter two number :
60
85
x = 10
y = 50
x = 60
y = 85
The No. of object is : 2
*/