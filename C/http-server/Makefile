CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
MAIN = http-server

.PHONY: default
default: http-server 


.PHONY: clean
clean:
	rm -f *.o *~ a.out core http-server

.PHONY: all
all: clean $(MAIN)