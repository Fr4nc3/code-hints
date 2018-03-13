#include <stdio.h>

void print_binary(int x){
  int shift, i;
  
  int space = 0;
  for (i = 31; i >= 0; --i)
  {
    /*
    >>, shifts all of the bits in a value to the right a specified number of times
    */
    shift = x >> i;
    
    // add a space every four digits
    if (space == 4){
      printf(" ");
      space = 0; // set space to 0 to start again
    }
    
    /*
     The bitwise AND is does exactly that: it does an AND operation on the Bits.
    */
    if (shift & 1){
      printf("1");
    } else {
      printf("0");
    }
    // counting to group by 4
    ++space;
  }
  
  printf("\n"); // add a break at the end

}