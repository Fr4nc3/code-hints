#include <stdio.h>      /* for printf() and fprintf() */
#include <sys/socket.h> /* for socket(), connect(), send(), and recv() */
#include <arpa/inet.h>  /* for sockaddr_in and inet_addr() */
#include <stdlib.h>     /* for atoi() and exit() */
#include <string.h>     /* for memset() */
#include <unistd.h>     /* for close() */
#include <signal.h>     /* for signal() */
#include <sys/types.h>
#include <netdb.h>



#define MAXPENDING 5    /* Maximum outstanding connection requests */
#define BUF_SIZE 4096
#define MAX 1000
static void die(const char *s)
{
    perror(s);
    exit(1);
}

char * statusMessage(int status){
 char * message;
 switch(status) {
   case 200:
     message = "200 OK";
     break;
   case 400:
     message = "400 Bad Request";
     break;
   case 404:
     message = "404 Not Found";
     break;
   case 500:
     message = "500 Internal Server Error";
     break;
   case 501:
     message = "501 Not Implemented";
     break;
   case 522:
     message = "522 Connection Timed Out";
     break;
   default:
    message = "520 Unknown Error";

 }
  return message;
}
void responseMessage(int responseStatus, int clntSock){

    char printMessage [MAX];
    int sizeMessage;
    int sizeResult;
    char *message = statusMessage(responseStatus);

    sizeMessage = sprintf(printMessage,"HTTP/1.0 %s\r\n\r\n<html><body><h1>%s</h1></body></html>\r\n\r\n", message, message);
    if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
          perror("send() failed");
    }
}

int getHTTPServer(unsigned short echoServPort){

    int servSock;                    /* Socket descriptor for server */
    struct sockaddr_in echoServAddr; /* Local address */
    
    /* Create socket for incoming connections */
    
    if ((servSock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
        die("socket() failed");
    
    //printf(" sizeof(echoServAddr) %d\n",  sizeof(echoServAddr));
    /* Construct local address structure */
    memset(&echoServAddr, 0, sizeof(echoServAddr));   // Zero out structure
    echoServAddr.sin_family = AF_INET;                // Internet address family
    echoServAddr.sin_addr.s_addr = htonl(INADDR_ANY); // Any incoming interface
    echoServAddr.sin_port = htons(echoServPort);      // Local port

    /* Bind to the local address */
    if (bind(servSock, (struct sockaddr *)&echoServAddr, sizeof(echoServAddr)) < 0)
        die("bind() failed");

    /* Mark the socket so it will listen for incoming connections */
    if (listen(servSock, MAXPENDING) < 0)
        die("listen() failed");
        
    return servSock;

}

int getMDBServer(char *mdbHost, unsigned short mdbPort){

    int sock;
    struct sockaddr_in serverAddr;
    struct hostent *he;

    // get server ip from server name
    if ((he = gethostbyname(mdbHost)) == NULL) {
	    die("gethoatbyname failed");
    }
    
    char *serverIP = inet_ntoa(*(struct in_addr *)he->h_addr);

    // create socket
    if ((sock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0) {
	      die("socket failed");
    }
    
    //printf("sizeof(serverAddr) %d\n", sizeof(serverAddr));
    // construct server address
    memset(&serverAddr, 0, sizeof(serverAddr));
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_addr.s_addr = inet_addr(serverIP);
    serverAddr.sin_port = htons(mdbPort);

    // connect
    if (connect(sock, (struct sockaddr *)&serverAddr, sizeof(serverAddr)) < 0) {
	    die("connect failed");
    }
    
    return sock;

}

void saveLog(char *requestIP, int responseStatus, char *requestLog){
  /*
  128.59.22.109 "GET /cs3157/tng/images/ship.jpg HTTP/1.1" 200 OK
  ip "requestLog" statusMessage
  */
 fprintf(stdout, "%s \"%s\" %s\n", requestIP,
                requestLog, statusMessage(responseStatus));
 fflush(stdout);

}

void mdbRequest(int mdbServer, int clntSock, FILE * mdbFile, char *requestURI, char *requestIP, char *requestLog){

     int responseStatus = 200;
    //http://the.host.name:8888/mdb-lookup?key=hello
    const char *form =
                "<h1>mdb-lookup</h1>\n"
                "<p>\n"
                "<form method=GET action=/mdb-lookup>\n"
                "lookup: <input type=text name=key>\n"
                "<input type=submit>\n"
                "</form>\n"
                "</p>\n";
                
    char printMessage [BUF_SIZE];
    int sizeMessage;
    int sizeResult;
    char *message = statusMessage(responseStatus);

    char *keyWord;
    keyWord = strrchr(requestURI, '=');
    if (keyWord == NULL){
       
        sizeMessage = sprintf(printMessage,"HTTP/1.0 %s\r\n\r\n<html><body>%s</body></html>\r\n\r\n", message, form);
        if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
                  perror("send() failed");
                  responseStatus = 500;
        }
    }else{
    
          keyWord++; // move from = word
            // wrap the socket with a FILE* so that we can read the socket using fgets()     
          //printf("keyword: %s\n", keyWord);  

          
         strcat(keyWord, "\n"); // this make it work
         
         if (send(mdbServer, keyWord, strlen(keyWord), 0) != strlen(keyWord)){
      			perror("send() failed");
      		  responseStatus = 500;
    		}
       
        if(responseStatus == 200){
        
          sizeMessage = sprintf(printMessage,"HTTP/1.0 %s\r\n\r\n", message);
          if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
                    perror("send() failed");
                    responseStatus = 500;
          }
          
          sizeMessage = sprintf(printMessage,"<html><body>\n%s<p><table border>\n", form);
         
          if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
                  perror("send() failed");
                  responseStatus = 500;
          }
          
          int i = 1;
          char line[MAX];
          char *bgcolor = "";
           for (;;) {
              if (fgets(line, sizeof(line), mdbFile) == NULL) {
                  if (ferror(mdbFile)){
                        perror("lookup error");
                      }
              }
              if((line[0] == '\r' && line [1] == '\n' ) || line [0] == '\n' ){
              			break;
              }
                  
              bgcolor = (i % 2 == 0)? "#cccccc": "";
              sizeMessage = sprintf(printMessage,"<tr><td bgcolor='%s'>%s</tr></td>\n", bgcolor, line);
              if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
                    perror("send() failed table return");
                    responseStatus = 500;
               }
          		 ++i;
           }

        
         sizeMessage = sprintf(printMessage,"</table></p></body></html>\n"); // close html
         if ((sizeResult = send(clntSock, printMessage, sizeMessage, 0)) != sizeMessage) {
                  responseStatus = 500;
                  saveLog(requestIP, responseStatus, requestLog);
                  perror("send() failed");
         }
        
        }
    }

    saveLog(requestIP, responseStatus, requestLog);
    if(responseStatus != 200){
       responseMessage(responseStatus, clntSock);     
    }
    
}

void httpRequest(int httpServer, int clntSock, char *webRoot, char *requestURI, char *requestIP, char *requestLog){
   int responseStatus = 200; // let start with ok!
   char printMessage [BUF_SIZE];
   int sizeMessage;
   int sizeResult;
   char *method = "rb";
   if (requestURI[strlen(requestURI)-1] == '/') {
    strcat(requestURI, "index.html");
  } 
  
  if(strstr(requestURI, "index.html")!=NULL){
     method = "r";

  }
  //printf("%s\n", requestURI);
	char *fullPath = (char *)malloc(strlen(webRoot) + strlen(requestURI) + 1);
	if (fullPath  == NULL){
    responseStatus = 500; 
	}
 
  if(responseStatus == 200){
  
      sprintf(fullPath, "%s", webRoot);
	    strcat(fullPath, requestURI);
      //printf("%s\n", fullPath);
      
      //printf("%s\n", method);
    	FILE *file = fopen(fullPath, method);
    	if (file == NULL){
    		free(fullPath);
    	  responseStatus = 404;
    	}
     
      if(responseStatus == 200){
         	sizeMessage = sprintf(printMessage, "HTTP/1.0 200 OK\r\n\r\n");
          if (send(clntSock, printMessage, sizeMessage, 0) != sizeMessage) {
            responseStatus = 500;
        		free(fullPath);
        		fclose(file);
            saveLog(requestIP, responseStatus, requestLog);
        		perror("send() failed header request");
        	}
        
         if(responseStatus == 200){
             char fileBuffer[BUF_SIZE];
             while ((sizeResult = fread(fileBuffer, 1, sizeof(fileBuffer), file)) > 0) {
               if (send(clntSock, fileBuffer, sizeResult, 0) != sizeResult) {
                      responseStatus = 500;
                  		free(fullPath);
                  		fclose(file);
                      saveLog(requestIP, responseStatus, requestLog);
                  		perror("send() failed while loop");
              		}
            	}
            
            	if (ferror(file)){
                  responseStatus = 500;
              		free(fullPath);
              		fclose(file);
              		perror("send() failed");
            	}
         }
      }
     if(fullPath){
    	free(fullPath);
     }
     if(file){
    	 fclose(file);
      }
  }
  
    saveLog(requestIP, responseStatus, requestLog);
    if(responseStatus !=200){
       responseMessage(responseStatus, clntSock);     
    }
}

int main(int argc, char *argv[])
{
    if (argc != 5) {
        fprintf(stderr, "%s\n", "Usage: http-server <server_port> <web_root> <mdb-lookup-host> <mdb-lookup-port>");
        exit(1);
    }
    
    // CHANGE: ignore SIGPIPE so that we don't terminate when we call
    // send() on a disconnected socket.

    if (signal(SIGPIPE, SIG_IGN) == SIG_ERR) 
        die("signal() failed");

    unsigned short serverPort = atoi(argv[1]);
    char *webRoot = argv[2];
    char *mdbHost = argv[3];
    unsigned short mdbPort = atoi(argv[4]);

    // get the two server
    int httpServer = getHTTPServer(serverPort);
    int mdbServer = getMDBServer(mdbHost, mdbPort);
    
    FILE *mdbFile = fdopen(mdbServer, "r");
    if (mdbFile  == NULL) {
          die("mdbFile failed to open");
    }
    
    int clntSock;                    /* Socket descriptor for client */
    unsigned int clntLen;            /* Length of client address data struct */
    struct sockaddr_in echoClntAddr; /* Client address */
    
    char *token_separators = "\t \r\n"; // tab, space, new line
    char *method;
    char *requestURI;
    char *httpVersion;
    
    char requestLine[BUF_SIZE];
    int responseStatus =200;
    
    for(;;){// start the process infinite loop
        /* Set the size of the in-out parameter */
        clntLen = sizeof(echoClntAddr);

        /* Wait for a client to connect */
        if ((clntSock = accept(httpServer, (struct sockaddr *) &echoClntAddr, &clntLen)) < 0){
            die("accept() failed");
        }
        
       // CHANGE: wrap the socket with a FILE* using fdopen()
        FILE *input = fdopen(clntSock, "r"); 
        if (input == NULL) 
           	die("fdopen failed");
    
        char *requestIP = inet_ntoa(echoClntAddr.sin_addr);
        
        printf("requestLine %s\n", requestLine);
        
        if (fgets(requestLine, sizeof(requestLine), input) != NULL) {
              perror("requestline");
              //fclose(input);
             //continue;
        }
        
        method = strtok(requestLine, token_separators);
        requestURI = strtok(NULL, token_separators);
        httpVersion = strtok(NULL, token_separators);

        //printf("method %s\n", method);
        //printf("requestURI %s\n", requestURI);
        //printf("httpVersion %s\n", httpVersion);
 
 
        char requestLog[sizeof(requestLine)+1];
      	sprintf(requestLog, "%s %s %s", method, requestURI, httpVersion);
       
       // printf("requestLog %s\n", requestLog);
      	if (method == NULL || requestURI == NULL || httpVersion == NULL){
            responseStatus = 501;
            //saveLog(requestIP, responseStatus, requestLog);
            //responseMessage(responseStatus, clntSock);
            perror("null values");
            fclose(input);
            continue;
        }

        if (strcmp(method, "GET") != 0 || (strcmp(httpVersion, "HTTP/1.0") != 0 && 
            strcmp(httpVersion, "HTTP/1.1") != 0)){
            responseStatus = 501;
            saveLog(requestIP, responseStatus, requestLog);
            responseMessage(responseStatus, clntSock);
            fclose(input);
            continue;
        }
        //1
        // no double dot allowed and not starting different than /
        printf("%s\n\n", requestURI);
        if (*requestURI != '/' || strstr(requestURI, "/..") != NULL) {
            //printf("dots");
            //tested and only goes default page:
            responseStatus = 400;
            saveLog(requestIP, responseStatus, requestLog);
            responseMessage(responseStatus, clntSock);
            fclose(input);
            continue;
        }

        if(responseStatus ==200){
          if (strstr(requestURI, "mdb-lookup") != NULL) { // if  contains mdb-lookup
              mdbRequest(mdbServer, clntSock, mdbFile,requestURI, requestIP, requestLog);
          }else{
              httpRequest(httpServer, clntSock, webRoot, requestURI, requestIP, requestLog);
          }
        }else{
            responseMessage(responseStatus, clntSock);
        }
        
        if(input){
          fclose(input); // close socket at the end
        }
    }// foreverloop
    // close at the end lookup file
    fclose(mdbFile);
  return 0;
}