#include "gcd.h"
int gcd(int x, int y){
    int t;
    while(y != 0){
       t = x;
       x = y;
       y = t%y;
    }
    /* return the latest value of x from the loop */
    return x;
}
