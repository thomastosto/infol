#include <stdio.h>

// . saisir deux valeurs (variables a et b), en faisant en sorte que a < b
// . saisir une troisième valeur (variable x), qui doit être entre a et b
// . déterminer de quelle extrémité x est le plus proche, puis donner cette valeur à la variable x.


void valx(int* x,int a,int b){
    //printf("%d %d",a,b);
    //int x;
    while(*x>b||*x<a){
        printf("rentrez une valeur x\n");
        scanf("%d",x);
    }
    if((a-*x)>(b-*x)){
        printf("La valeur x %d est plus proche de b %d que de a %d \n",*x,b,a);
        *x=b;
    }
    else{
        printf("La valeur x %d est plus proche de a %d que de b %d \n",*x,a,b);
        *x=a;
        
    }
    //return x;
}
int main(){
    int a,b;
    int x;
    int temp;
    printf("saisissez deux valeurs entières\n");
    scanf("%d %d",&a,&b);
    if(a>b){
        temp=b;
        b=a;
        a=temp;
    }
    //x=valx(a,b);
    valx(&x,a,b);
    printf("la  nouvelle valeur de x est %d",x);
    return 0;
}