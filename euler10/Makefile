CPPFLAGS=-I.
CXXFLAGS=-g

all: euler10

euler10: euler10.o bigint.o
	$(LINK.C) -o $@ $^

euler10.o: bigint.h
bigint.o: bigint.h

clean:
	rm *.o
