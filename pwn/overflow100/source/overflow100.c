#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdbool.h>

// Define our user struct containing our attributes
struct user_s {
	char name[16];
	bool is_admin;
};

int main()
{
	// Exit the program after 30 seconds
	alarm(30);

	// Make sure output isn't buffered to ensure a smooth user experience
	setvbuf(stdout, NULL, _IONBF, 0);

	// Important parts below:
	struct user_s user;
	user.is_admin = false;

	printf("Welcome to my first attempt at using structs in C!\nWhat's your name?: ");

	gets(user.name);

	if(user.is_admin) {
		printf("Welcome! This is the secret admin area, take your complimentary flag!\n");
		system("/bin/cat flag.txt");
	} else {
		printf("Sorry, this application is for admins only!\n");
	}

	return 0;
}
