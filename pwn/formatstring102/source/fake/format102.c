#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
	// Why take more input than needed?...
	char buf[16] = { 0 };

	// Exit the program after 30 seconds
	alarm(30);

	// Make sure output isn't buffered to ensure a smooth user experience
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Welcome to my third attempt at taking user input in C! This time with some restrictions...\nThis program will printf any text you give it :)\n\n");

	// Important parts below:
	while (1) {
		printf("Input: ");
		if (!fgets(buf, sizeof(buf), stdin)) {
			perror("fgets()");
			exit(EXIT_FAILURE);
		}

		printf("Output: ");
		// UwU what's this?
		char* flag = "PLACEHOLDER FLAG! Real flag is on the remote server ;)";
		printf(buf);
	}
	return 0;
}
