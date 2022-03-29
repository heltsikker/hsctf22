# HS-CTF-22
Helt Sikker CTF 2022

## Challenges

### Web

- Vaccine - SQLi
- Girl Scouts - Cookie modification
- Bradley Urglar's API - Insecure direct object reference (from NAV IT)
- Repo - CVE-2021-22205 gitlab RCE
- Protectr - robots.txt
- Inspector Gadget - Flag in page source

### Crypto

- Long lost message - Playfair cipher
- Hexadecimal - Hex to ASCII
- Exclusive Or - XOR with known key
- Mario 64 - Base64
- Old School Crypto - Caesar cipher
- RSA - Fermat attack on RSA
- Access Not Authorized - MAC forgery (from Simula UiB)
- CatCoin - Schnorr's protocol with weakness (from Simula UiB)

### Reversing

- sgnirtS - Flag checker binary without protection.
- Break - Flag checker where flag is decrypted before comparing with input.
- Break all you want - Flag checker where the input is xored and compared with the encrypted flag.
- We need the Admin hash - Decrypt firmware blob and find password hash (from mnemonic)

### Pwn

- Format String 100 - printf challenge solved with %s
- Format String 101 - printf challenge solved with %x %x %x %x %x %x %s
- Format String 102 - printf challenge solved with %7$s
- Format String 200 - printf challenge solved with %69c%n
- Buffer Overflow 100 - BOF challenge solved with any input longer than 16 characters
- Buffer Overflow 101 - BOF challenge with specific byte input to solve
- Unwinnable - Basic BOF with uncalled function to print the flag
- Call Me Maybe - Simple ROP where you have to call 3 functions in the correct order to print the flag
- Shellcode - Program that executes any shellcode given to it

### Misc

- Listening - Wireshark pcapng with plain text TCP flag
- Chat mignon - Stego challenge from NAV IT
- Blame - Git impersination challenge. (Currently needs manual verification of success. Not sure how to automatically give a flag).
- PR - Flag in promo posters and headers
- Road to Lindesnes - Stego challenge
- Airplanes - OSINT challenge based on historical satellite imagery
- Walkie Talkie - SDR FM audio data
- Radio Waves - Digital SDR data (from mnemonic)
- Can you Crack it? - NTLM password cracking (from mnemonic)
- Greatest Shell - pcap analysis lvl 1 (from Netsecurity)
- Bruteforce Madness - pcap analysis lvl 2 (from Netsecurity)
- Port Scan Deluxe - pcap analysis lvl 3 (from Netsecurity)
- Fire Beat - Exif data in audio file

### Physical

- Lockpicking 1
- Lockpicking 2
- Lockpicking 3
- Lockpicking 4
- Lockpicking 5
- Circuit - Read schematic to figure out the "password" on an FPGA board
- Intercept - Grab wpa2 wifi handshake and crack the password

