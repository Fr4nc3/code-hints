#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mylist.h"
#include "mdb.h"

static void die(const char *message)
{
    perror(message);
    exit(1); 
}

static void printString(void *p)
{
     struct MdbRec * d = (struct MdbRec *) p;
     printf("{%s} said {%s}\n", d->name, d->msg);
}

int main(int argc, char **argv)
{

  if(argc != 2){
    die("usage: mdb-lookup <database_file>");
  }
  struct List list;
  
  
  argv++; // move the pointer to the db-name
  char *filename = *argv;

  FILE *fp = fopen(filename,"rb"); // file opening
  if (!fp){
    die("Error to open the db");
  }
  
  initList(&list);
  loadmdb(fp, &list);

  fclose(fp); // close it bc it is already load it 
  //traverseList(&list, &printString); // print list
  printf("\n");

  
  char lookup[1000]; 
  printf("lookup: ");
  while(fgets(lookup, sizeof(lookup), stdin) != NULL){ 
    int count;
    struct Node *test;
    
    int len = strlen(lookup);
    if(len > 1 ){
      count = 1;
      test = list.head;
      char word[6];
      //strncpy(word, lookup, 5);
      
      if(len>5){
        strncpy(word, lookup, 5);
        word[5] = '\0'; 
      }else{
        strncpy(word, lookup, len-1); // now works!!!
        word[len-1] = '\0'; // magic line
      }
      //printf("%s", word);

      while (test != NULL){
        struct MdbRec *d = (struct MdbRec *) test->data;
        //strcasestr case insensitive, mdb-lookup from the professor is case sensitive 
        //but I think it is better case insensitive 
        if (strcasestr(d->name, word) != NULL || strcasestr(d->msg, word) != NULL){
          // print if it is fine
          printf("%d:", count);
          printString(test->data);
        }
        /* loop the list */
        test = test->next; 
        ++count;
      }
    }else{
     
      count = 1;
      test = list.head;
      while (test != NULL){
        printf("%d:", count);
        printString(test->data); 
        test = test->next; 
        ++count;
      }
    }

   printf("lookup: ");
  }

  printf("\n"); // 
  freemdb(&list);
  return 0;
}