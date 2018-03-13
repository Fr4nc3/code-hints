/*
 * twecho
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
void uppercase(char *str){
   int i = 0;
   while(str[i]!= '\0'){
     /* convert character by character to upper case */
      str[i] = toupper(str[i]);
      ++i;
   }
}

static char **duplicateArgs(int argc, char **argv)
{
     int i;
     /*  create the allocated memmory for the array of words */
     char **newArgs = malloc((argc+1) * sizeof(char*));
     /* check if we don't run out of memmory */
     if (newArgs == NULL){
        perror("malloc returned NULL");
        exit(1);
     }
  
    for (i = 0; i < argc; ++i){
        /* create the allocated memmory for the word */
         *(newArgs + i) = malloc((strlen(argv[i])+1) * sizeof(char));
        /* check if we don't run out of memmory */
        if (*(newArgs + i) == NULL){
          perror("malloc returned NULL");
          exit(1);
        }
        /* copy the existing word */
        strcpy(*(newArgs + i), argv[i]);
        /*  convert the new (copied) word in uppercase */
        uppercase(*(newArgs + i));
     }
     // professor gave the hint in lab2 description see README.txt
     *(newArgs + i) = NULL; 
     return newArgs;
}

static void freeDuplicatedArgs(char **copy)
{
    char **a;
    for (a = copy; *a != NULL; ++a){
     /* free each allocated memmory for each word */
     free(*a);
    }
    /* free the memmory for the array of words */
    free(copy);
}

/*
 * DO NOT MODIFY main().
 */
int main(int argc, char **argv)
{
    if (argc <= 1)
        return 1;

    char **copy = duplicateArgs(argc, argv);
    char **p = copy;
    
    argv++;
    p++;
    while (*argv) {
        printf("%s %s\n", *argv++, *p++);
    }

    freeDuplicatedArgs(copy);

    return 0;
}
