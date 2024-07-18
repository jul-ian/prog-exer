// 1. Saying Hello

#include <stdio.h>
#define MAX_LEN 80

int main(void) {
    int n_char = 0;
    char name[MAX_LEN], input_char;
    printf("What is your name? ");
    while(((input_char = getchar()) != '\n') && n_char < MAX_LEN) {
        name[n_char++] = input_char;
    }
    printf("Hello, ");
    for(int i = 0; i < n_char; i++) {
        printf("%c", name[i]);
    }
    printf(", nice to meet you!\n");
    return 0;
}
