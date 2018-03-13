INCLUDE = -I../../linkedlist
LDFLAGS = -g -L../../linkedlist
CC = gcc
CFLAGS = -g -Wall $(INCLUDE)
MAIN = mdb-lookup

LDLIBS = -lmylist 

$(MAIN): mdb-lookup.o mdb.o
	gcc $(LDFLAGS) mdb-lookup.o mdb.o $(LDLIBS)-o $(MAIN)

mdb-lookup.o: mdb-lookup.c mdb.h
	gcc $(CFLAGS) -c -o mdb-lookup.o mdb-lookup.c

mdb.o: mdb.c mdb.h
	gcc $(CFLAGS) -c -o mdb.o mdb.c

.PHONY: clean
clean:
	rm -f *.o *~ a.out core $(MAIN)

.PHONY: all
all: clean $(MAIN)
