CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
MAIN = twecho

$(MAIN): twecho.o 
	gcc $(LDFLAGS) twecho.o -o $(MAIN)

twecho.o: twecho.c 
	gcc $(CFLAGS) -c -o twecho.o twecho.c

.PHONY: all
all: clean main

.PHONY: clean
clean:
	rm -f *.o $(MAIN) 