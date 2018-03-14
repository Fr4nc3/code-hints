Francia F. Riesco 
ff2214
lab 9
part1
======

a)
ff2214@paris:~/cs3157/lab9$ ./test4
BASIC4TRACE: (0x7fff35644770)->MyString(const char *)   :line 13,constructor, x
BASIC4TRACE: (0x7fff35644780)->MyString(const char *)   :line 14, constructor y
BASIC4TRACE: (0x7fff356447b0)->MyString(const MyString&):line 5, copy constructor, a
BASIC4TRACE: (0x7fff356447a0)->MyString(const MyString&):line 5, copy constructor, b
BASIC4TRACE: (0x7fff35644720)->MyString(const char *)   :line 7, constructor, t
BASIC4TRACE: op+(const MyString&, const MyString&)      :line 8, operator+, a + t,
BASIC4TRACE: (0x7fff356446d0)->MyString()               :line 8, constructor,  a + t
BASIC4TRACE: (0x7fff35644730)->MyString(const MyString&):line 8, copy constructor, a + t t copy to a variable this variable will be operator+ to b
BASIC4TRACE: (0x7fff356446d0)->~MyString()              :line 8, Destructor. a + t 
BASIC4TRACE: op+(const MyString&, const MyString&)      :line 8, operator+, temporary-variable + b entering op+
BASIC4TRACE: (0x7fff356446d0)->MyString()               :line 8, temporary-variable + b  MyString constructor for temporary variable
BASIC4TRACE: (0x7fff35644740)->MyString(const MyString&):line 8, temporary-variable + b copy constructor  new value to be operator+ to b
BASIC4TRACE: (0x7fff356446d0)->~MyString()              :line 8,  temporary-variable + b destructor temporary variable
BASIC4TRACE: (0x7fff356447c0)->MyString(const MyString&):line 16, copy constructor, temporary variable result of add method
BASIC4TRACE: (0x7fff35644740)->~MyString()              :line 9, AKA end of the method add destructur temporary variable created in + b 
BASIC4TRACE: (0x7fff35644730)->~MyString()              :line 9, AKA end of the method add destructur temporary a + t 
BASIC4TRACE: (0x7fff35644720)->~MyString()              :line 9, AKA end of the method add destructur t 
BASIC4TRACE: (0x7fff35644790)->MyString(const MyString&):line 16, copy constructor, z 
BASIC4TRACE: (0x7fff356447c0)->~MyString()              :line 16, destructor, of temporary variable result of add 
BASIC4TRACE: (0x7fff356447a0)->~MyString()              :line 16, destructor, parameter y in add never used again got destroyed
BASIC4TRACE: (0x7fff356447b0)->~MyString()              :line 16, destructor, parameter x in add never used again got destroyed
one and two                                             :line 17, print z cout << z << endl;
BASIC4TRACE: (0x7fff35644790)->~MyString()              :line 19, AKA end of main method: destructor, z
BASIC4TRACE: (0x7fff35644780)->~MyString()              :line 19, AKA end of main method: destructor, y 
BASIC4TRACE: (0x7fff35644770)->~MyString()              :line 19, AKA end of main method: destructor, x

b)
ff2214@paris:~/cs3157/lab9$ ./test4
BASIC4TRACE: (0x7fffb6f51670)->MyString(const char *)
BASIC4TRACE: (0x7fffb6f51680)->MyString(const char *)
BASIC4TRACE: (0x7fffb6f51620)->MyString(const char *)
there is no copy reference of x and y because they were passed as reference 
BASIC4TRACE: op+(const MyString&, const MyString&)
BASIC4TRACE: (0x7fffb6f515d0)->MyString()
BASIC4TRACE: (0x7fffb6f51630)->MyString(const MyString&)
BASIC4TRACE: (0x7fffb6f515d0)->~MyString()
BASIC4TRACE: op+(const MyString&, const MyString&)
BASIC4TRACE: (0x7fffb6f515d0)->MyString()
BASIC4TRACE: (0x7fffb6f51640)->MyString(const MyString&)
BASIC4TRACE: (0x7fffb6f515d0)->~MyString()
BASIC4TRACE: (0x7fffb6f516a0)->MyString(const MyString&)
BASIC4TRACE: (0x7fffb6f51640)->~MyString()
BASIC4TRACE: (0x7fffb6f51630)->~MyString()
BASIC4TRACE: (0x7fffb6f51620)->~MyString()
BASIC4TRACE: (0x7fffb6f51690)->MyString(const MyString&)
BASIC4TRACE: (0x7fffb6f516a0)->~MyString()
there is no destructor call for a and b in method add because they were passed as reference of x and y 
one and two
BASIC4TRACE: (0x7fffb6f51690)->~MyString()
BASIC4TRACE: (0x7fffb6f51680)->~MyString()
BASIC4TRACE: (0x7fffb6f51670)->~MyString()

c) 
http://linux.die.net/man/1/g++
-fno-elide-constructors
The C ++ standard allows an implementation to omit creating a temporary which is only used to initialize another object of the same type. Specifying this option disables that optimization, and forces G++ to call the copy constructor in all cases.
g++ -O0  -g -Wall -DBASIC4TRACE   -c -o test4.o test4.cpp
g++ -g  test4.o mystring.o   -o test4
./test4

BASIC4TRACE: (0x7fffb254ae40)->MyString(const char *)
BASIC4TRACE: (0x7fffb254ae50)->MyString(const char *)
BASIC4TRACE: (0x7fffb254ae00)->MyString(const char *)
BASIC4TRACE: op+(const MyString&, const MyString&)
BASIC4TRACE: (0x7fffb254adb0)->MyString()
it doesn't create and destroy temporary variables for a + t 
BASIC4TRACE: (0x7fffb254ae10)->MyString(const MyString&)
BASIC4TRACE: (0x7fffb254adb0)->~MyString()
BASIC4TRACE: op+(const MyString&, const MyString&)
BASIC4TRACE: (0x7fffb254adb0)->MyString()
it doesn't created and destroy temporary vairbales for temprary + b
BASIC4TRACE: (0x7fffb254ae60)->MyString(const MyString&)
BASIC4TRACE: (0x7fffb254adb0)->~MyString()
BASIC4TRACE: (0x7fffb254ae10)->~MyString()
BASIC4TRACE: (0x7fffb254ae00)->~MyString()
one and two
BASIC4TRACE: (0x7fffb254ae60)->~MyString()
BASIC4TRACE: (0x7fffb254ae50)->~MyString()
BASIC4TRACE: (0x7fffb254ae40)->~MyString()
there are less  constructor and copy contructor and destrouctor call because there are no temporary variable were created. 

part2
=====
a) 
//<, >, ==, !=, <=, >=
add test5.cpp to Makefile
b) 
I was having this error
make
g++ -O0 -fno-elide-constructors -g -Wall -DBASIC4TRACE   -c -o test1.o test1.cpp
In file included from test1.cpp:1:0:
mystring.h:56:47: error: 'MyString& operator+=(const MyString&)' must take exactly two arguments
make: *** [test1.o] Error 1

then 
removed operator+ locationg comment out friend


