main: var.o principale.o
	gcc principale.o var.o -o main
principale.o: principale.c  var_struct.h 
	gcc principale.c -c
var.o: var_struct.h var_struct.c 
	gcc var_struct.c -c