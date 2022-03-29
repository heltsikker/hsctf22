#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void win() {
	system("/bin/cat flag.txt");
}

void lose() {
	printf("Wrong word! You lose!\n");
}

void play() {
	char buf[32];

	printf("Welcome to my unwinnable game! All you have to do to win is guess what word I'm thinking of! I promise I won't change my mind ;)\n\nWhat word am I thinkin of?: ");

	gets(buf);

	return;
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	play();
	lose();

	return 0;
}
