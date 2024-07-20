#include <stdio.h>
#define MAX_STR_LEN 80

int main(void) {
    int n = 0;
    char user_str[MAX_STR_LEN], user_char;
    printf("What is the input string? ");
    while((user_char = getchar()) != '\n' && n < MAX_STR_LEN) {
        user_str[n++] = user_char;
    }
    for(int i = 0; i < n; i++) {
        printf("%c", user_str[i]);
    }
    printf(" has %d characters.\n", n);
    return 0;
}
