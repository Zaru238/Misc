#! /usr/bin/make -f

.DEFAULT_GOAL := run

run: a.out
	./a.out

a.out: main.cpp
	g++ main.cpp

clean:
	rm -rf a.out
