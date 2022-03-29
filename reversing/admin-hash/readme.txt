# Category: Misc/Reversing

# Title: We need the Admin hash

# Author: mnemonic

# Description: 

This firmware of this Wifi enabled IP camera has been "encrypted" by using XOR, can you decrypt the firmware, extract the filesystem and retreieve the Administrators password hash?

#Downloadable File: 
IC3116W_encrypted.bin.zip


# Flag 
HSCTF{$1$yAn92Ld/$u%nHFH9nLds0naDaLuK1d/}


# Hint
XOR encryption has a flaw if the keylenght is shorter than the file it is being encrypted. 
If you hex hard enough, you should be able to find the key. 

# Difficulty: Medium


