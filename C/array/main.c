#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "sort_integer.h"

int main(){
  int size;
  printf("Please enter the size of the array:\n");
  scanf("%d", &size); /* get the size variable */

  int *array;
  /* Allocate memmory for the new array */
  array=(int *) malloc(size * sizeof(int));
  /* Check out of memmory */
  if (array == NULL) {
        perror("malloc returned NULL");
        exit(1);
  }
  
  int i;
  int *pa = array;   
  srandom(time(NULL));
  
  /* Populate the new array with random numbers */
  for(i=0; i < size; i++) {
    *pa = random();
     pa++;
  }

  /* Allocate memmory for the new array */
  int *array1;
  array1 = (int *) malloc(size * sizeof(int));
  /* Check out of memmory */
  if (array1 == NULL) {
        perror("malloc returned NULL");
        exit(1);
  }
  /* Populate the second array with the elements of the first array */
  mycopy(array1, array, size);

  int *pa1 = array1; 
  int *p = &array1[size-1]; // last element pointer
  /* Sort the second array ascending  */
  sort_integer_array(pa1, p, 1);
  
  /* Allocate memmory for the new array */
  int *array2;
  array2 = (int *) malloc(size * sizeof(int));
  /* Check out of memmory */
  if (array2 == NULL) {
        perror("malloc returned NULL");
        exit(1);
  }
  /* Populate the third array with the elements of the first array */
  mycopy(array2, array, size);

  int *pa2 = array2; 
  int *p2 = &array2[size-1]; // last element pointer
  /* Sort the third array descending  */
  sort_integer_array(pa2, p2, 0);

  
    /* Print the Array */
  printf("First Array:\n");
  for(i=0; i < size; i++) {
     printf("%d\n", array[i]);
  }
  
  /* Print second array */
  printf("\nSecond Array:\n");
  for(i=0; i < size; i++) {
     printf("%d \n", array1[i]);
  }
  
  /* Print the third aray*/
  printf("\nThird Array:\n");
  for(i=0; i < size; i++) {
     printf("%d \n", array2[i]);
  }
  /* free memmory */
  free(array);
  free(array1);
  free(array2);

  return 0;
}