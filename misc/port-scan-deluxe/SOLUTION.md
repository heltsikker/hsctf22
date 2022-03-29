1. Look at the destination ports from the attacker
2. This will show a clear raising pattern from 1-2000, except for certain points
3. If you for example use the following to retrive the dest ports: `tshark -Y "ip.dst==10.13.37.4" -T fields -e tcp.dstport -r help.pcapng`

Find the location where something is suddenly a bit jumbled around. This is the flag in ord() values.

```
62
63
64
65
66
67
68
69
70
72
83
67
84
70
123
100
111
110
116
95
109
```

Decode this using any tool and you will get the flag.
