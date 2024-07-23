#include <stdio.h>
#include <string.h>
#define MAX_STR_LEN 80

int main() {
    int i = 0, j = 0;
    char user_chr;
    char quote[MAX_STR_LEN], author[MAX_STR_LEN];
    printf("What is the quote? ");
    while((user_chr = getchar()) != '\n') {
        if(i < MAX_STR_LEN - 1) {
            quote[i] = user_chr;
        } 
        else break;
    }
    quote[i] = '\0';
    printf("Who said it? ");
    while((user_chr = getchar()) != '\n') {
        if(j < MAX_STR_LEN - 1) {
            author[i] = user_chr;
        }
        else break;
    }
    author[j] = '\0';
    printf("%s says, \"%s\"", author, quote);
    return 0;
}
