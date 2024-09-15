#include <stdio.h>
// void aviscore(){
//     int score;
//     printf("Rentrez un score\n");
//     scanf("%d",&score);
//     if (score<200){
//         printf("C'est catastrophique");
//     }
//     else if((score >=200)&&(score<5000)){
//         printf("tu peux mieux faire");
//     }
//     else{
//         printf("Tu es le meilleur ");
//     }
// }
void compte(){
    int nbcoup;
    printf("Rentrez un nombre de coup\n");
    scanf("%d",&nbcoup);
    if(nbcoup>1){
        printf("Vous avez fait %d coups",nbcoup);
    }
    else
        printf("Vous avez rentre %d coup",nbcoup);
}
int main(){
    //aviscore();
    compte();
    return 0;
}