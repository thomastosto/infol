#ifndef VAR_TRUCT_H
#define VAR_STRUCT_H
#include <stdio.h>
#include <stdlib.h>

typedef struct var{
    int ent;
    double reel;
}var;

//Ecrivez une fonction echanger permettant d'échanger les contenus de telles variables.
//3) Ecrivez une fonction ordonner permettant d'ordonner les contenus de telles variables selon la
//valeur de leur champ entier.
//Vous pouvez écrire deux versions de cette fonction : sans utiliser la fonction echange / en l'utilisant.
//4) Ecrivez une fonction ordonner3 permettant d'ordonner les contenus trois de ces variables.
//Nb : Vous pouvez utiliser la fonction ordonner (ou pas)
void creer(var* v,int ent,double reel);
void afficher(var v);
void echanger(var* a,var*b);
void ordonner(var*a,var*b);
void ordonner3(var*a,var*b,var*c);
#endif