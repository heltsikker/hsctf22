#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	char *buf;
	buf = mmap(0, 1024, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
	puts("Give me up to 1024 bytes of shellcode and I'll execute it, and that's a guarantee!");
	read(0, buf, 1024);
	(*(void(*)()) buf)();
	return 0;
}
