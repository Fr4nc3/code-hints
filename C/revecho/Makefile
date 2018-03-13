INCLUDE = -I ../part1
LDFLAGS = -g -L ../part1
CC = gcc
CFLAGS = -g -Wall $(INCLUDE) 
MAIN = revecho

LDLIBS = -lmylist 

revecho: revecho.o 

revecho.o: revecho.c

.PHONY: clean
clean:
	rm -f *.o  $(MAIN)

.PHONY: all
all: clean $(MAIN)