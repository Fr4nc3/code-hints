#include <cassert>
#include "mystring.h"
int main(){
  // test cases
  MyString s1("hello");
  MyString s2("world!");
  //these tests are all true
  assert(s1 < s2);
  assert(!(s1 > s2));
  assert(!(s1 ==  s2));
  assert(s1 !=  s2);
  assert(s1 <=  s2);
  assert(!(s1 >=  s2));
  assert(s1 ==  "hello");
  assert("hello" ==  s1);

  MyString s("hello");
  s += " world";
  cout << s << endl;

  // test op+=() and op+()
  MyString sp(" ");
  MyString period(".");
  MyString str;
  str += "This" + sp + "should" + sp
  += "work" + sp + "without"
  += sp + "any" + sp + "memory"
  += sp + "leak"
  += period;
  cout << str << endl;

  return 0;
}