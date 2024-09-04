#include <stdio.h>
#include <stdlib.h>
#include "temps.c"
int main(){
    temps tm;
    tm=creer(11,65,75);
    // saisir(&tm);
    // afficher(tm);
    //printf("%d",correct(tm));
    normaliser(&tm);
    afficher(tm);
}