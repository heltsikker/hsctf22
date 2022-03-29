CC=gcc

.PHONY: all, clean
all: shellcode

shellcode: shellcode.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -vf shellcode
