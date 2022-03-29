1. Take a look at the attempted passwords in the POST requests to the getUsersBlogs
2. This will not be possible to find without some scripting, so get grep or tshark out and filter those packets
3. Get the password values, and just scroll through the results and you will find a flag.
4. Dirty method: `strings help.pcapng | grep getUsersBlogs | cut -d ">" -f15 | cut -d "<" -f1`

```
baby123
slayer
angelita
love1
alexa
H
S
C
T
F
{
b
r
u
t
e
f
o
r
c
```