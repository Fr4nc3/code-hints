// test4.cpp

#include "mystring.h"

static MyString add(const MyString& a, const MyString& b)
{
    MyString t(" and ");
    return a + t + b;
}

int main()
{
    MyString x("one");
    MyString y("two");

    MyString z = add(x, y);
    cout << z << endl;
    return 0;
}
