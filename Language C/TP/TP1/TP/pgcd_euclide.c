#include <stdio.h>
#include <stdlib.h>

int main(){
    int a,b,pgcd,r;
    printf("Rentrez une valeur a pour le calcul du PGCD a doit être supérieur à b\n");
    scanf("%d",&a);
    printf("Rentrez une valeur b pour le calcul du PGCD a doit être supérieur à b\n");
    scanf("%d",&b);
    int i=1;
    // while(i<=b){
    //     if(b%i==0&&a%i==0){
    //         pgcd=i;
    //     }
    //     i++;
    // }
    //printf("le PGCD de a et b est %d \n",pgcd);
    for(int j=1;j<=b;j++){
        r=a%b;
        if(r!=0){
            a=b;
            b=r;
        }
    }
    printf("le PGCD de a et b est %d \n",b);
    return 0;
}