#include <stdio.h>
#include <stdlib.h>
#include "var_struct.c"
// A
//  3.01 , B 6
//  4.3 , C −2
//  10.0 ,
int main(){
    var A,B,C;
    creer(&A,7,3.01);
    creer(&B,6,4.3);
    creer(&C,-2,10.0);
    // afficher(A);
    // afficher(B);
    // echanger(&A,&B);
    // afficher(A);
    // afficher(B);
    ordonner3(&A,&B,&C);
    afficher(A);
    afficher(B);
    afficher(C);
}