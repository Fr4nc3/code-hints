#include "mylist.h"
#include <stdlib.h>
#include <stdio.h>

struct Node *addFront(struct List *list, void *data){

    struct Node *mynode = (struct Node*) malloc (sizeof (struct Node));
    
    if (mynode == NULL){
       return NULL;
    }
    
    mynode->data = data; // assign data
    mynode->next = list->head; // set next the head of the list
    list->head = mynode; // set the head the new node
    
    return mynode; // return the new node

}

void traverseList(struct List *list, void (*f)(void *)){
//traverseList(&list, &printDouble);
   struct Node *test = list->head;
    while (test != NULL){// while is not the last element of the list
      (*f)(test->data); //cast the function passing the parameter
      test = test->next; // move to the next element
    }

}

struct Node *findNode(struct List *list, const void *dataSought,
	int (*compar)(const void *, const void *)){
  /*
    example how works
    x = 3.5;
    node = findNode(&list, &x, &compareDouble);*/
    if (list->head == NULL){
      return NULL; // empty list
    }
    
    // if list is not empty get the first as a pointer
    struct Node *test = list->head;
    while (test != NULL){
      if((*compar)(test->data, dataSought) == 0){// data == datasought
        return test;// return the node
      }
      test = test->next; // move to the next element
    }
    return NULL; // in case goes to all the while-loop without finding
}

void flipSignDouble(void *data){

  /*
  first we get the real value of data and we cast double
  we multiply -1 
  we assign the new value to data 
  */
  *(double*)data = (double)-1 * (*(double*)data);

}

int compareDouble(const void *data1, const void *data2){

 /*if the difference is not zero they are not equal*/
  if ((*(double*)data1 - *(double*)data2 ) != 0 ){
    return 1;
  }else{
    return 0;
  }
}

void *popFront(struct List *list){

  if(isEmptyList(list) == 1){ //if the list is empty nothing to do
    return NULL;
  }
  struct Node *nextFromHead = (*list).head->next; // get the next from head
  void *poppedData = (*list).head->data;
  
  free((*list).head); // free memmory used by head
  (*list).head = nextFromHead;//set the new head
  
  return poppedData; 
}

void removeAllNodes(struct List *list){

  while(isEmptyList(list)!=1){
    popFront(list);// remove the first element until the end of the lsit
  }

}

struct Node *addAfter(struct List *list, 
	struct Node *prevNode, void *data){
 
     if (prevNode == NULL) {
      return addFront(list, data); 
    }
    //printf("%.1f", *(double *)data);
    
    struct Node *mynode = (struct Node*) malloc (sizeof (struct Node));
    //node = addAfter(&list, node, a+i);
    if (mynode == NULL){
       return NULL;
    }

    mynode->data = data; // assign the data to the new node

    struct Node *prevNodeNext = prevNode->next; //a node to hold the prevNodeNext 
    prevNode->next = mynode; // now the next of the prevNode is the new node
    mynode->next = prevNodeNext; // in the test is always null
    
    return mynode;  
    
}

void reverseList(struct List *list){

      struct Node *prev = NULL;
      struct Node *current = list->head;
      struct Node *next;

      while (current != NULL) { // move the pointer backward
        next = prev; // next is now preveous
        prev = current; // preveous is the actual or current
        current = current->next; // current is the next
        prev->next = next; // and the one that was prev is the next 
      }
      
      list->head = prev;// last reversed element hit from lab3 document
}