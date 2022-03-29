#CC=gcc -m32
CC=gcc
#CC=clang # sometimes, gcc puts unwanted stuff on the stack, then try this one
CFLAGS=-Wall -Wextra
CFLAGS+=-fno-stack-protector # disable stack cookies
CFLAGS+=-z execstack # disable NX
CFLAGS+=-no-pie # disable randomising of addresses
CFLAGS+=-Wl,-z,norelro # disable RELRO (GOT is writeable)

.PHONY: all, clean
all: overflow101

overflow101: overflow101.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -vf overflow101
