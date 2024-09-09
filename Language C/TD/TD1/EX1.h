#include <stdio.h>
#ifndef EX1_H
#define EX1_H
void echanger(int* var1,int* var2){
    int temp;
    temp=*var1;
    *var1=*var2;
    *var2=temp;
}
void ordonner(int* a,int* b){
    if(*a>*b){
        echanger(a,b);
    }
}
void ordonner3(int*a,int*b,int*c){
   while((*(a)>*(b))||(*(b)>*(c))){
        if(*a>*b){
            ordonner(a,b);
        }
        else if(*b>*c){
            ordonner(b,c);
        }
    }
}
void minmax(int a, int b, int c){
    ordonner3(&a,&b,&c);
    printf("le minimum est %d et le maximum %d",a,c);
}
#endif