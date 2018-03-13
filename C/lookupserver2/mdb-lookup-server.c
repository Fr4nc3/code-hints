#include <stdio.h>      /* for printf() and fprintf() */
#include <sys/socket.h> /* for socket(), connect(), send(), and recv() */
#include <arpa/inet.h>  /* for sockaddr_in and inet_addr() */
#include <stdlib.h>     /* for atoi() and exit() */
#include <string.h>     /* for memset() */
#include <unistd.h>     /* for close() */
#include <signal.h>     /* for signal() */

#define MAXPENDING 5    /* Maximum outstanding connection requests */

#include "mylist.h"
#include "mdb.h"

#define MAX 1000
#define KeyMax 5

static void die(const char *s)
{
    perror(s);
    exit(1);
}

int loadmdb(FILE *fp, struct List *dest) 
{
    /*
     * read all records into memory
     */

    struct MdbRec r;
    struct Node *node = NULL;
    int count = 0;

    while (fread(&r, sizeof(r), 1, fp) == 1) {

        // allocate memory for a new record and copy into it the one
        // that was just read from the database.
        struct MdbRec *rec = (struct MdbRec *)malloc(sizeof(r));
        if (!rec)
            return -1;
        memcpy(rec, &r, sizeof(r));

        // add the record to the linked list.
        node = addAfter(dest, node, rec);
        if (node == NULL) 
            return -1;

        count++;
    }

    // see if fread() produced error
    if (ferror(fp)) 
        return -1;

    return count;
}

// from lab4 solutions too
void freemdb(struct List *list) 
{
    // free all the records
    traverseList(list, &free);
    removeAllNodes(list);
}

void handleTCPClient(int clntSock, char *dbfile){

      //
      
        FILE *fp = fopen(dbfile, "rb");
        if (fp == NULL) 
            die(dbfile);

        struct List list;
        initList(&list);
    
        int loaded = loadmdb(fp, &list);
        if (loaded < 0)
            die("loadmdb");
        
        fclose(fp);

        /*
         * lookup loop
         */
        // from lab4 solutions
        char line[MAX];
        char key[KeyMax + 1];
        char printMessage [MAX];
        
        // variables to check the size of buffer
        int sizeMessage;
        int sizeResult;
        
        FILE *in = fdopen (clntSock, "r");
    		if (in == NULL) {
          die ( "fdopen  failed" );
        }
        
        // read from the fdopen file
    		while (fgets(line, sizeof (line), in) != NULL)
    		{
           // must null-terminate the string manually after strncpy().
            strncpy(key, line, sizeof(key) - 1);
            key[sizeof(key) - 1] = '\0';
    
            // if newline is there, remove it.
            size_t last = strlen(key) - 1;
            if (key[last] == '\n')
                key[last] = '\0';
    
            // traverse the list, printing out the matching records
            struct Node *node = list.head;
            int recNo = 1;
            while (node) {
                
                struct MdbRec *rec = (struct MdbRec *)node->data;
                if (strstr(rec->name, key) || strstr(rec->msg, key)) {
                   // printf("%4d: {%s} said {%s}\n", recNo, rec->name, rec->msg);
                   //sprintf(printMessage, "%4d: {%s} said {%s}\n", recNo, rec->name, rec->msg);
		               //send (clntSock, printMessage, strlen(printMessage), 0 );  
                       
               		sizeMessage = sprintf(printMessage, "%4d: {%s} said {%s}\n", recNo, rec->name, rec->msg);
              		if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
              		    perror("send() failed");
              		    break;
              		}                        
                }
                
                node = node->next;
                recNo++;
            }// while node
            // print newline 
           	sizeMessage = sprintf(printMessage, "\n");
            if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage){
               perror("send() failed");
            }
	                
        }// while line
        
        if (ferror(in)) {
	          die("fgets failed");
        }
        
        // close what it is open
        fclose (in);
        freemdb(&list);

}


int main(int argc, char *argv[])
{
    // from lab6 requirement 
    // ignore SIGPIPE so that we don�t terminate when we call
    // send() on a disconnected socket.
    if (signal(SIGPIPE, SIG_IGN) == SIG_ERR){
        die("signal() failed");
    }
    // if the parameters are not coming 
    if (argc != 3) {
        fprintf(stderr, "%s\n", "Usage: mdb-lookup-server <database_file> <server port>");
        exit(1);
    }
    
    // from TCPechoServer
    int servSock;                    /* Socket descriptor for server */
    int clntSock;                    /* Socket descriptor for client */
    struct sockaddr_in echoServAddr; /* Local address */
    struct sockaddr_in echoClntAddr; /* Client address */
    unsigned short echoServPort;     /* Server port */
    unsigned int clntLen;            /* Length of client address data structure */

    char *dbfile = argv [1];
	  echoServPort = atoi(argv[2]);
     
     //from TCPechoServer
    /* Create socket for incoming connections */
    if ((servSock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0){
      die("socket() failed");
    }
        
    // from TCPechoServer
    /* Construct local address structure */
    memset(&echoServAddr, 0, sizeof(echoServAddr));   /* Zero out structure */
    echoServAddr.sin_family = AF_INET;                /* Internet address family */
    echoServAddr.sin_addr.s_addr = htonl(INADDR_ANY); /* Any incoming interface */
    echoServAddr.sin_port = htons(echoServPort);      /* Local port */

    /* Bind to the local address */
    if (bind(servSock, (struct sockaddr *) &echoServAddr, sizeof(echoServAddr)) < 0)
        die("bind() failed");

    /* Mark the socket so it will listen for incoming connections */
    if (listen(servSock, MAXPENDING) < 0)
        die("listen() failed");

    for (;;) /* Run forever */
    {
    
         // from TCPEchoServer
        /* Set the size of the in-out parameter */
        clntLen = sizeof(echoClntAddr);
        // from TCPEchoServer
        /* Wait for a client to connect */
        if ((clntSock = accept(servSock, (struct sockaddr *) &echoClntAddr, 
                               &clntLen)) < 0){
              die("accept() failed");                 
        }
            
        // from TCPEchoServer
        /* clntSock is connected to a client! */
        printf("Handling client %s\n", inet_ntoa(echoClntAddr.sin_addr));
         // from TCPEchoServer + file
        handleTCPClient(clntSock, dbfile);
    }

  return 0;
}