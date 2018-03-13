CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
MAIN = main

.PHONY: default
default: all run

$(MAIN): main.o prime.o gcd.o
	gcc $(LDFLAGS) main.o prime.o gcd.o -o $(MAIN)

main.o: main.c prime.h gcd.h
	gcc $(CFLAGS) -c -o main.o main.c

prime.o: prime.c prime.h
	gcc $(CFLAGS) -c -o prime.o prime.c

gcd.o: gcd.c gcd.h
	gcc $(CFLAGS) -c -o gcd.o gcd.c

.PHONY: all
all: clean main

.PHONY: clean
clean:
	rm -f *.o $(MAIN) 

.PHONY: run
run:
	./$(MAIN)