main: calcul.o main.o
	gcc main.o calcul.o -o main
main.o: main.c calcul.h
	gcc main.c -c
calcul.o: calcul.h calcul.c 
	gcc calcul.c -c