#include "calcul.h"
#include <stdlib.h>
#include <math.h>
#define max(a,b) (((a)>(b)) ? (a):(b))
#define min(a,b) (((a)<(b)) ? (a):(b))
void afficher(int a, int b){
    printf("le maximum des deux valeurs est %d et le minimum est %d",max(a,b),min(a,b));
}
//saisir recursif au lieu d'un while et pour faire à la fois pour a et b sans avoir à ecrire deux fois la saisie 
void saisir(int* nb){
    do{
        printf("Entrez une valeur : ");
        int e=-1;
        while(e!=1){
            e=scanf("%d", nb)==1;
            printf("Vous devez saisir un nombre !");
        }
        
    }
}