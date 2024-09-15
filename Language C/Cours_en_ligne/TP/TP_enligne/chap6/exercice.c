#include <stdio.h>
void premier(){
    int val,i,nbdiv=0;
    i=2;
    printf("rentez une valeur pour que je teste si c'est un nombre premier\n");
    scanf("%d",&val);
    while(i<val&& (val%i!=0)){
        i++;
    }
    if(i==val){
        printf("le nombre %d est premier",val);
    }
    else{
       printf("le nombre %d n'est pas premier",val);
    }
}
int main(){
    premier();
    return 0;
}