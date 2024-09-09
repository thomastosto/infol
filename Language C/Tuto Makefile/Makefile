main: hello.o main.o
	gcc main.o hello.o -o main
main.o: main.c hello.h
	gcc main.c -c
hello.o: hello.h hello.c
	gcc hello.c -c