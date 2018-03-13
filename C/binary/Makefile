CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
MAIN = convert

$(MAIN): main.o binary.o
	gcc $(LDFLAGS) main.o binary.o -o $(MAIN)

main.o: main.c binary.h
	gcc $(CFLAGS) -c -o main.o main.c

binary.o: binary.c binary.h
	gcc $(CFLAGS) -c -o binary.o binary.c

.PHONY: all
all: clean main

.PHONY: clean
clean:
	rm -f *.o $(MAIN) 