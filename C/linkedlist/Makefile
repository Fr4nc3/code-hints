CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g
MAIN = mylist-test

mylist-test: mylist-test.o libmylist.a 
	gcc -g mylist-test.o -L. -lmylist -o $(MAIN)

mylist-test.o: mylist-test.c mylist.h

mylist.o: mylist.c mylist.h 

libmylist.a: mylist.o 
	ar rc libmylist.a mylist.o
	ranlib libmylist.a

.PHONY: clean
clean:
	rm -f *.o libmylist.a $(MAIN)

.PHONY: all
all: clean $(MAIN)