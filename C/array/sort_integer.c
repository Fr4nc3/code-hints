#include "sort_integer.h"
#include <stdlib.h>
#include <stdio.h>

/* compare ascending two int */
int asc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}
/* compare ascending two int */
int desc (const void * a, const void * b)
{
   return ( *(int*)b - *(int*)a );
}

/* This function sorts an integer array.
begin points to the 1st element of the array.
end points to ONE PAST the last element of the array.
If ascending is 1, the array will be sorted in ascending order.
If ascending is 0, the array will be sorted in descending order.
*/


void sort_integer_array(int *begin, int *end, int ascending)
{
/* In here, you will call your real sorting function (your own
* or the qsort()). Basically, I want to make sure that you
* know how to translate the begin/end parameter to whatever
* is required for your sorting function.
*/
  int size = 1;
  int first = *begin;
  /* the way that I found to have the number of elements to sort */
  while(first != *end--){
    ++size;
  }
  /* differenciate the sorting ascending or descending */
  if(ascending == 1){
    qsort(begin, size, sizeof(int), asc);
  }else{
    qsort(begin, size, sizeof(int), desc);
  }
  
}

void mycopy(int *s, int *t, int size){
  int i;
  /*  copy version from the book K&R2 with 
   while give an error this way doesnt*/
  for (i = 0 ;i < size; ++i){
   *s++ = *t++;
  }
}