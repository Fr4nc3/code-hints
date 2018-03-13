#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <netdb.h>

#define BUFSIZE   4096

static void die(const char *s)
{
    perror(s);
    exit(1);
}

int main(int argc, char *argv[])
{
    // if the parameters are not coming 
    if (argc != 4) {
        fprintf(stderr, "%s\n", "usage: http-client <host name> <port number> <file path>");
        fprintf(stderr, "%s\n", "ex) http-client www.example.com 80 /index.html");
        exit(1);
    }
    
    struct hostent *he;
    char *serverName = argv[1];
    char *serverPort =  argv[2];
    char *filePath = argv[3];
    char *fileName = strrchr(filePath, '/'); // file name start at /
    fileName++;
    // from lab6 part2 requirement 
    // get server ip from server name
    if ((he = gethostbyname(serverName)) == NULL) {
      die("gethoatbyname failed");
    }
    
    char *serverIP = inet_ntoa(*(struct in_addr *)he->h_addr);
    
    
    // from TCPechoServer
    int servSock;                    /* Socket descriptor for server */
    struct sockaddr_in echoServAddr; /* Local address */
    unsigned short echoServPort;     /* Server port */

	  echoServPort = atoi(serverPort);
     
     //from TCPechoServer
    /* Create socket for incoming connections */
    if ((servSock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0){
      die("socket() failed");
    }
        
    // from TCPechoServer
    /* Construct local address structure */
    memset(&echoServAddr, 0, sizeof(echoServAddr));   /* Zero out structure */
    echoServAddr.sin_family = AF_INET;                /* Internet address family */
    echoServAddr.sin_addr.s_addr = inet_addr(serverIP); /*IP */
    echoServAddr.sin_port = htons(echoServPort);      /* Local port */
    
    if (connect(servSock, (struct sockaddr *)&echoServAddr, sizeof(echoServAddr)) < 0) {
      	die("connection error");
    }
    
    char *header;
    char buffer[BUFSIZE];

    // I was getting headers issues as bad request so this header fix it
    header =  "GET %s HTTP/1.0\r\nHost: %s:%s\r\n\r\n";

    snprintf(buffer, sizeof(buffer), header, filePath, serverName, serverPort);
    if (send(servSock, buffer, strlen(buffer), 0) != strlen(buffer)) {
	    die("send error");
    }
    
    FILE *in = fdopen (servSock, "r");
    if (in == NULL) {
       die("fdopen  failed");
    }
    
    if(fgets(buffer, sizeof(buffer), in) == NULL){
        die(buffer);
    }
    
    if(strstr(buffer, "200") == NULL || strstr(buffer, "HTTP/1") == NULL){ //cover http/1.0 and http/1.1
        fclose(in); // I was getting valgrind issues
        die(buffer);
    }
    
    //printf("%s\n", buffer);
    // read from the fdopen file
    while (fgets(buffer, sizeof(buffer), in) != NULL)
    {
       if(strcmp(buffer, "\r\n") == 0){
         break; // move out of the header
       }
    }

    FILE *out = fopen(fileName, "w");
    if (out == NULL)
        die("fopen() failed");
    
    int sizeMessage;
    while((sizeMessage = fread(buffer, 1, sizeof(buffer), in)) > 0){
        if (fwrite(buffer, 1, sizeMessage, out) != sizeMessage){
          die("writting file error");
        }    
    }
    
    if (ferror(in)) {
       die("fgets failed");
    }
    // close the files
    fclose(in);
    fclose(out);
  return 0;
}