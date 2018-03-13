/*
 * mdb-lookup-server-nc-2.c
 */

#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <unistd.h>
#include <ctype.h>
#include <ctype.h>

#define KeyMax 6

static void die(const char *s)
{
    perror(s);
    exit(1);
}

int main(int argc, char **argv)
{
    char port[100]; // similar to lab4 
    char key[KeyMax + 1];
    pid_t pid; 
    printf("port number: ");
    fflush(stdout);
    while (fgets(port, sizeof(port), stdin) != NULL) {
    
    
        if(strlen(port)>1){// only enter if the port value is long
               strncpy(key, port, sizeof(key) - 1); // from lab4 solutions
               key[sizeof(key) - 1] = '\0';  // from lab4 solutions
              
              // if newline is there, remove it.
              // I took this from lab4 
              size_t last = strlen(key) - 1;  // from lab4 solutions
              if (key[last] == '\n') //  // from lab4 solutions
                  key[last] = '\0';

              pid = fork();
                  
              if (pid < 0) { // from part1.b
          	    die("fork failed");
              } else if (pid == 0) {// from part1.b modified to 

                	fprintf(stderr, "[pid=%d] ", (int)getpid());
                	fprintf(stderr, "mdb-lookup-server started on port %s\n", key);
                	execl("./mdb-lookup-server-nc.sh", "mdb-lookup-server-nc.sh", key, (char *)0);
                	die("execl failed");
              } 
              
              while((pid = waitpid((pid_t) -1, NULL, WNOHANG)) > 0){
                  fprintf(stderr, "[pid=%d] ", (int)pid);
                  fprintf(stderr, "mdb-lookup-server terminated\n");
              } 
                      
        }
        
      if(port[0]=='\n'){ // only prompt when user enter ENTER
         printf("port number: ");
         fflush(stdout); 
      }
    }

return 0;
}