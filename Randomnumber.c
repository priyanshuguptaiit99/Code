#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(0));

    int randomnumber = (rand() % 100) + 1;
    int noofguesses = 0;
    int guessed;

    do{
        printf("Guess The number: ");
        scanf("%d", &guessed);
        if(guessed>randomnumber){
            printf("Enter lower number\n");
        }

        else if(guessed<randomnumber){
            printf("Enter higher number\n");
        }

        else if(guessed=randomnumber){
            printf("Congrats you enter correct number\n");
        }

        noofguesses++;    
        }
        while (guessed!=randomnumber);

        printf("You guessed the number in %d guess", noofguesses);

    return 0;
}