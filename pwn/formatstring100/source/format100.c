#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	char buf[128] = { 0 };

	// Exit the program after 30 seconds
	alarm(30);

	// Make sure output isn't buffered to ensure a smooth user experience
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Welcome to my first attempt at taking user input in C!\nThis program will printf any text you give it :)\n\n");

	// Important parts below:
	while (1) {
		printf("Input: ");
		if (!fgets(buf, sizeof(buf), stdin)) {
			perror("fgets()");
			exit(EXIT_FAILURE);
		}

		printf("Output: ");
		// UwU what's this?
		printf(buf, "HSCTF{user_input_should_never_be_trusted!}");
	}
	return 0;
}
