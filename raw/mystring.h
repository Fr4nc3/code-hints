#ifndef __MYSTRING_H__
#define __MYSTRING_H__

#include <iostream>

using namespace std;

class MyString {

   public:

	// default constructor
	MyString();

	// constructor
	MyString(const char* p);

	// destructor
	~MyString();

	// copy constructor 
	MyString(const MyString& s);

	// copy assignment
	MyString& operator=(const MyString& s);

	// returns the length of the string
	int length() const { return len; }
	
	// operator+ unfriend lab9 part2b 
	//friend MyString operator+(const MyString& s1, const MyString& s2);

	// put-to operator
	friend ostream& operator<<(ostream& os, const MyString& s);

	// get-from operator
	friend istream& operator>>(istream& is, MyString& s);

	// operator[]
	char& operator[](int i);

	// operator[] const
	const char& operator[](int i) const;

  //new code lab9 part2a 
  //<, >, ==, !=, <=, >=

	friend int operator<(const MyString& s1, const MyString& s2);
	friend int operator>(const MyString& s1, const MyString& s2);
	friend int operator==(const MyString& s1, const MyString& s2);
	friend int operator!=(const MyString& s1, const MyString& s2);
	friend int operator<=(const MyString& s1, const MyString& s2);
	friend int operator>=(const MyString& s1, const MyString& s2);

  // operator+= lab9 part2b
  MyString& operator+=(const MyString& s);
  private:

	char* data;

	int len;
};

// operator+ lab9 part2b
MyString operator+(const MyString& s1, const MyString& s2);

#endif
