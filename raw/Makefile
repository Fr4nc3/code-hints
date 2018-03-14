# use the new C++ compiler, clang++, which has a better C++11 support
CC  = clang++
CXX = clang++

INCLUDES =

CFLAGS   = -g -Wall $(INCLUDES)
CXXFLAGS = -g -Wall $(INCLUDES) -std=c++11

LDFLAGS = -g
LDLIBS  =

twecho2: duper_upper.o

twecho2.o: duper_upper.h

duper_upper.o: duper_upper.h

.PHONY: clean
clean:
	rm -f *.o twecho2

.PHONY: all
all: clean twecho2

.PHONY: valgrind
valgrind: all 
	valgrind --leak-check=yes --track-origins=yes ./twecho2 hello world
