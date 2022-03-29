#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(void)
{
	char buf[128] = { 0 };

	// Exit the program after 30 seconds
	alarm(30);

	// Make sure output isn't buffered to ensure a smooth user experience
	setvbuf(stdout, NULL, _IONBF, 0);

	printf("Welcome to my FOURTH attempt at taking user input in C... Now with even better protected secrets!\nThis program will printf any text you give it (as long as it doesn't contain my favorite letter) :)\n\n");

	// Important parts below:
	while (1) {
		printf("Input: ");
		if (!fgets(buf, sizeof(buf), stdin)) {
			perror("fgets()");
			exit(EXIT_FAILURE);
		}

		// Check if the buffer contains my top secret favorite letter
		if (strchr(buf, 'E') != 0) {
			printf("Sorry that input isn't allowed!\n");
			break;
		}

		printf("Output: ");
		printf(buf, buf);

		// Only reveal my secret to those who know my favorite letter
		if (strchr(buf, 'E') != 0) {
			printf("HSCTF{woah_you_can_write_values_to_memory_by_printing_user_input??}\n");
		}
	}
	return 0;
}
