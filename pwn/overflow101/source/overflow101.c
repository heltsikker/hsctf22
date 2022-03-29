#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

// Define our user struct containing our attributes
struct user_s {
	char name[16];
	int user_type;
};

int main()
{
	// Exit the program after 30 seconds
	alarm(30);

	// Make sure output isn't buffered to ensure a smooth user experience
	setvbuf(stdout, NULL, _IONBF, 0);

	// Important parts below:
	struct user_s user;
	user.user_type = 0;

	printf("Welcome to my second attempt at using structs in C! Now with less corruptible variable types!\nWhat's your name?: ");

	gets(user.name);

	if(user.user_type == 1337) {
		printf("Welcome! This is the secret admin area, take your complimentary flag!\n");
		system("/bin/cat flag.txt");
	} else {
		printf("Sorry, this application is for admins only!\nAdmin type: 1337\nYour type: %d\n", user.user_type);
	}

	return 0;
}
