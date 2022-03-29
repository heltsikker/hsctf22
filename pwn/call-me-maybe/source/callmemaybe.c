#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int (*function)(const char*) = &puts;
char* argument = "Hey, I just met you!";

void hey_i_just_met_you() {
	char buf[32];
	
	printf("Hey I just met you! Do you know the rest of the lyrics?: ");

	gets(buf);

	return;
}

void and_this_is_crazy() {
	argument = "/bin/cat flag.txt";
}

void but_heres_my_number() {
	function = &system;
}

void so_call_me_maybe() {
	function(argument);
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	hey_i_just_met_you();

	printf("Wrong lyrics, bye bye!");

	return 0;
}
