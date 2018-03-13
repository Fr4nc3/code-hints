#include "prime.h"

int prime(int x){
    /* if it is divided by 2 is not prime*/
    if(x%2==0){
        return 0;
    }
    /* only check if the odd numbers can devide the number*/
    int i;
    for(i=3; i*i <= x; i+=2){
        if(x%i==0){
            return 0;
        }
    }
    /* if it is prime*/
    return 1;
}
