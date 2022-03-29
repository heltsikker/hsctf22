#Solution

The file `cutecat.png` contains additional data after the `IEND` chunk (which normally terminates png's). Most viewer programs ignore this data, making the image appear as if everything is normal.

This extra chunk of data can be extracted manually using tools like [xxd](https://linux.die.net/man/1/xxd) or [hexedit](https://linux.die.net/man/1/hexedit), or you can use more automated tools like [binwalk](https://www.kali.org/tools/binwalk/).

The output from `binwalk cutecat.png` looks like this:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 900 x 962, 8-bit colormap, non-interlaced
187           0xBB            TIFF image data, big-endian, offset of first image directory: 8
379           0x17B           Zlib compressed data, best compression
250999        0x3D477         Zip archive data, encrypted at least v2.0 to extract, compressed size: 4898, uncompressed size: 6044, name: flag.webp
256059        0x3E83B         End of Zip archive, footer length: 22
```
revealing that the png also contains a password protected zip file. 

`binwalk -e cutecat.png` will extract the content into its own folder.

Hints for finding the password can be found in the Exif data. 

```
❯ exiftool cutecat.png
....
Artist                          : 1337_haX0r
....
GPS Position                    : 45 deg 36' 27.15", 4 deg 4' 4.06"
```

If you Google the GPS position after converting it from degrees/minutes/seconds to decimal degrees (45.607541395194616 4.067793556242393) you will end up at the "PassWord" store in the `Montbrison` (which is also the zip password) county in France.

Extract the zip to get the file `flag.webp`.
