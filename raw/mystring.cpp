#include <cstring>
#include <cstdio>

#include "mystring.h"

// default constructor

MyString::MyString() 
{
#ifdef BASIC4TRACE
    fprintf(stderr, "BASIC4TRACE: (%p)->MyString()\n", this);
#endif

    data = new char[1];
    data[0] = '\0';
    
    len = 0;
}

// constructor

MyString::MyString(const char* p)
{
#ifdef BASIC4TRACE
    fprintf(stderr, "BASIC4TRACE: (%p)->MyString(const char *)\n", this);
#endif

    if (p) {
	len = strlen(p);
	data = new char[len+1];
	strcpy(data, p);
    } else {
	data = new char[1];
	data[0] = '\0';
	len = 0;
    }
}

// destructor

MyString::~MyString() 
{
#ifdef BASIC4TRACE
    fprintf(stderr, "BASIC4TRACE: (%p)->~MyString()\n", this);
#endif

    delete[] data;
}

// copy constructor 

MyString::MyString(const MyString& s) 
{
#ifdef BASIC4TRACE
    fprintf(stderr, "BASIC4TRACE: (%p)->MyString(const MyString&)\n", this);
#endif

    len = s.len;
    
    data = new char[len+1];
    strcpy(data, s.data);
}

// copy assignment

MyString& MyString::operator=(const MyString& rhs)
{
#ifdef BASIC4TRACE
    fprintf(stderr, "BASIC4TRACE: (%p)->op=(const MyString&)\n", this);
#endif

    if (this == &rhs) {
	return *this;
    }

    // first, deallocate memory that 'this' used to hold

    delete[] data;

    // now copy from rhs
    
    len = rhs.len;

    data = new char[len+1];
    strcpy(data, rhs.data);

    return *this;
}

// operator+

/*MyString operator+(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op+(const MyString&, const MyString&)\n");
#endif
    // old implemention
    
    MyString temp;

    delete[] temp.data;

    temp.len = s1.len + s2.len;

    temp.data = new char[temp.len+1];
    strcpy(temp.data, s1.data);
    strcat(temp.data, s2.data);

    return temp;
}*/

// put-to operator

ostream& operator<<(ostream& os, const MyString& s)
{
    os << s.data;
    return os;
}

// get-from operator

istream& operator>>(istream& is, MyString& s)
{
    // this is kinda cheating, but this is just to illustrate how this
    // function can work.
    
    string temp;
    is >> temp;

    delete[] s.data;

    s.len = strlen(temp.c_str());
    s.data = new char[s.len+1];
    strcpy(s.data, temp.c_str());

    return is;
}

// operator[] - in real life this function should be declared inline

char& MyString::operator[](int i) 
{
    return data[i];
}

// operator[] const - in real life this should be inline

const char& MyString::operator[](int i) const
{
    // illustration of casting away constness
    return ((MyString&)*this)[i];
}

//new code lab9 part2a 
//<, >, ==, !=, <=, >=

int operator<(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op<(const MyString&, const MyString&)\n");
#endif

  return (strcmp(s1.data, s2.data) < 0);
}

int operator>(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op>(const MyString&, const MyString&)\n");
#endif

  return (strcmp(s1.data, s2.data) > 0);
}

int operator==(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op==(const MyString&, const MyString&)\n");
#endif

  return (strcmp(s1.data, s2.data) == 0);
}

int operator!=(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op!=(const MyString&, const MyString&)\n");
#endif
  return  !(s1 == s2); // this uses operator == and !
}

int operator<=(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op<=(const MyString&, const MyString&)\n");
#endif
  return !(s1 > s2); // this uses operator > and !
}

int operator>=(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op>=(const MyString&, const MyString&)\n");
#endif

  return !(s1 < s2); // this uses operator < and !
}

// operator +=
MyString& MyString::operator+=(const MyString& s)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op+=(const MyString&)\n");
#endif

    len += s.len;// new lenght
    char *temp = new char[len+1]; // temporary char array
    strcpy(temp, data);
    strcat(temp, s.data);
    delete [] data; // remove old data
    data = temp; // put new data
    return *this;
}

// new operator + 
MyString operator+(const MyString& s1, const MyString& s2)
{
#ifdef BASIC4TRACE
    fprintf(stderr, 
	    "BASIC4TRACE: op+(const MyString&)\n");
#endif
    MyString temp = s1;
    return temp += s2; // uses += for + operator
}

