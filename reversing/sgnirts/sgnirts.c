#include <stdio.h>
#include <string.h>

static char *flag = "HSCTF{strings_is_a_lifesaver}";

int main(void) {
    char input[100];

    printf("Enter the flag: ");
    scanf("%s", input);
    if (strcmp(flag, input) == 0) {
        printf("Correct!\n");
    }
    else {
        printf("Incorrect flag...\n");
    }
}
