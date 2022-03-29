CC=gcc

.PHONY: all, clean
all: format100

format100: format100.c
	$(CC) $(CFLAGS) $^ -o $@
	cp $^ fake/
	sed -i "s/HSCTF{.*}/PLACEHOLDER FLAG! Real flag is on the remote server ;)/" fake/$^
	$(CC) $(CFLAGS) fake/$^ -o fake/$@

clean:
	rm -vf format100 fake/*
