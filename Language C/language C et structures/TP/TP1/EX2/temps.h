// #pragma once
#ifndef TEMPS_H
#define TEMPS_H
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct temps{
    int heures,minutes,secondes;
}temps;
//renvoie une variable de type struct temps créée avec les valeurs passées en paramètre
temps creer(int h, int m, double s);

// pour s'assurer que les champs ont tous une valeur positive (ou nulle)
_Bool correct(temps t);

//a chage, avec 2 positions pour les minutes et pour la partie réelle des secondes
void afficher (temps t);

// ramène les minutes et les secondes à une valeur strictement plus petite que 60
void normaliser(temps*);

// permet créer un struct temps en a ectant aux champs des valeurs lues au clavier 
temps creer2(void);

// permet à l'utilisateur de renseigner les champs d'un struct temps passé en paramètre 
void saisir(temps* pt);
#endif