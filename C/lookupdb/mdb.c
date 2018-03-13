#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "mylist.h"
#include "mdb.h"

int loadmdb(FILE *fp, struct List *dest){

  struct MdbRec record;
  struct Node *node = NULL;

  while(fread(&record, sizeof(struct MdbRec), 1, fp) != 0 ){
       /* allocate the mdbrec memory to storage the name and msg*/
       struct MdbRec *row = (struct MdbRec *)malloc(sizeof(struct MdbRec));
        if (row == NULL){
           perror("out of memort");
           exit(1);
        }
        //each record is struc MdbRec copy to the row
        strncpy(row->name, record.name, 16);
        strncpy(row->msg, record.msg, 24); 
        //printf("%s\n", row->name);// 
        node = addAfter(dest, node, row); //add the row to the list
        if(node == NULL){
           perror("out of memort");
           exit(1);
        }
   }

return 0;

}

void freemdb(struct List *list){
   while(!isEmptyList(list)){
        struct MdbRec *temp = popFront(list);
        free(temp);// free the element from memory
    }
}
