CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
MAIN = mytest

$(MAIN): mytest.o mylist.o
	gcc $(LDFLAGS) mytest.o mylist.o -o $(MAIN)

mytest.o: mytest.c mylist.h
	gcc $(CFLAGS) -c -o mytest.o mytest.c

mylist.o: mylist.c mylist.h
	gcc $(CFLAGS) -c -o mylist.o mylist.c

.PHONY: all
all: clean mytest

.PHONY: clean
clean:
	rm -f *.o $(MAIN) 