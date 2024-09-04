#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "temps.h"

//renvoie une variable de type struct temps créée avec les valeurs passées en paramètre
temps creer(int h, int m, double s){
    struct temps tm;
    tm.heures=h;
    tm.minutes=m;
    tm.secondes=s;
    return tm;
}

// pour s'assurer que les champs ont tous une valeur positive (ou nulle)
_Bool correct(temps t){
    bool cor=0;
    if(t.heures>=0&&t.minutes>=0&&t.secondes>=0){
        return cor=1;
    }
    return cor;
}

//a chage, avec 2 positions pour les minutes et pour la partie réelle des secondes
void afficher (temps t){
    if(t.minutes<10||t.secondes<10){
        printf("Le temps est :  %d : %.2d: %.2d",t.heures,t.minutes,t.secondes);
    }
    else{
        printf("Le temps est :  %d : %d: %d",t.heures,t.minutes,t.secondes);
    }
}

// ramène les minutes et les secondes à une valeur strictement plus petite que 60
void normaliser(temps* t){
    //temps tm;
    //tm=t;
    while(t->secondes>=60||t->minutes>=60){
        if(t->secondes>=60){
            t->minutes++;
            t->secondes%=60;
        }
        else if(t->minutes>=60){
            t->heures++;
            t->minutes%=60;
        } 
    }
    //afficher(t);
    //return t;
}
// permet créer un struct temps en affectant aux champs des valeurs lues au clavier 
temps creer2(void){
    temps tm;
    printf("rentrez un nombre d'heures\n");
    scanf("%d",&tm.heures);
    printf("rentrez un nombre minutes\n");
    scanf("%d",&tm.minutes);
    printf("rentrez un nombre secondes\n");
    scanf("%d",&tm.secondes);
    return tm;
}

// permet à l'utilisateur de renseigner les champs d'un struct temps passé en paramètre 
void saisir(temps* pt){
    temps tm;
    tm=creer2();
    pt->heures=tm.heures;
    pt->minutes=tm.minutes;
    pt->secondes=tm.secondes;
}