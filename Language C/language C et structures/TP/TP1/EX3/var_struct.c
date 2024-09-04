#include <stdio.h>
#include <stdlib.h>
#include "var_struct.h"
void creer(var* v,int ent,double reel){
    v->ent=ent;
    v->reel=reel;
}
void afficher(var v){
    printf("la partie entière du nombre est %d et sa partie reel est %.2f\n",v.ent,v.reel);
}
void echanger(var* a,var*b){
    var temp;
    temp=*a;
    *a=*b;
    *b=temp;
}
void ordonner(var*a,var*b){
    if(a->ent>b->ent){
        echanger(a,b);
    }
}
void ordonner3(var*a,var*b,var*c){
    while(((a->ent)>(b->ent))||((b->ent)>(c->ent))){
        if(a->ent>b->ent){
            ordonner(a,b);
        }
        else if(b->ent>c->ent){
            ordonner(b,c);
        }
    }
}