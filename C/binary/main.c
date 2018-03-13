#include <stdio.h>
#include "binary.h"

int main(){
  int x;
  scanf("%d", &x);
  /*
  Print integer x in different format
  */
  printf("signed dec:   %d\n", x);
  printf("unsigned dec: %u\n", x);
  printf("hex:          %x\n", x);
  printf("binnary:      ");
  
  print_binary(x);// call the method that print x in binary
  
  return 0;
}
