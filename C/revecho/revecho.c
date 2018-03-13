#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "mylist.h"
#include <string.h>

static void printString(void *p)
{
    printf("%s \n",(char *) p);// cast the pointer as char
}

int compareString(const void *data1, const void *data2){

 /*if the difference is not zero they are not equal*/
   const char *a = (const char*)data1;
   const char *b = (const char*)data2;
   return strcmp(a,b);
}

static void die(const char *message)
{
    perror(message); // I used from part1 
    exit(1); 
}

int main(int argc, char **argv)
{
    if (argc <= 1)
        return 1;
        
    struct Node *node; // for test dude
    struct List list;
    initList(&list); //start the list
    
    argv++;
    while (*argv) {
        if (addFront(&list, *argv++) == NULL){ // populate list
	          die("addFront() failed");
        }
    }
    
    traverseList(&list, &printString); // print list
    printf("\n");

    node = findNode(&list, "dude", &compareString);// search list 
    if(node == NULL){
      printf("dude not found\n");
    }else{
      printf("dude  found\n");
    }
    
    removeAllNodes(&list); // clear the memmory
  return 0;
}