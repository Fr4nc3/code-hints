#include <stdio.h>
#include "gcd.h"
#include "prime.h"

int main(){
  int x, y;
  printf("Please enter two integers:\n");
  scanf("%d%d",&x,&y); /* get the two variables */
  
  float avg = (float)(x+y)/2; /* convert to float to keep accuracy */
  
  printf("You typed in %d and %d \n", x, y);
  printf("The average is: %f \n", avg); /* all decimals */
  
  /* check if the integers are prime or not */
  int x_prime = prime(x);
  int y_prime = prime(y);

  if(x_prime == 1) {
    printf("%d is prime \n", x);
  } else {
    printf("%d is not prime \n", x);
  }
  
  if(y_prime == 1) {
    printf("%d is prime \n", y);
  } else {
    printf("%d is not prime \n", y);
  }
  
  /* check if the integers are gcd */
  int gcd_result = gcd(x, y);
  printf("the greatest common divisor is:  %d \n", gcd_result);
  
  return 0;
}