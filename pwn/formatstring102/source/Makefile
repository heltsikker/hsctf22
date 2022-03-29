CC=gcc

.PHONY: all, clean
all: format102

format102: format102.c
	$(CC) $(CFLAGS) $^ -o $@
	cp $^ fake/
	sed -i "s/HSCTF{.*}/PLACEHOLDER FLAG! Real flag is on the remote server ;)/" fake/$^
	$(CC) $(CFLAGS) fake/$^ -o fake/$@

clean:
	rm -vf format102 fake/*
