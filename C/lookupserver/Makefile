CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -g

.PHONY: default
default: mdb-lookup-server-nc-2 mdb-lookup-server-nc-1 


.PHONY: clean
clean:
	rm -f *.o *~ a.out core mdb-lookup-server-nc-1 mdb-lookup-server-nc-2 

.PHONY: all
all: clean $(MAIN)