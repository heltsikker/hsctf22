CC=gcc

.PHONY: all, clean
all: format101

format101: format101.c
	$(CC) $(CFLAGS) $^ -o $@
	cp $^ fake/
	sed -i "s/HSCTF{.*}/PLACEHOLDER FLAG! Real flag is on the remote server ;)/" fake/$^
	$(CC) $(CFLAGS) fake/$^ -o fake/$@

clean:
	rm -vf format101 fake/*
