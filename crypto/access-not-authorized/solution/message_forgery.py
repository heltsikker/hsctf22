message = "order=open_all_chests"
bytes_message = bytes(message, "utf-8")
mac = "50cb15dc7c9eac0d5532d78f3622c73d4369d803"

length_initial = len(bytes_message) + 16  # length in bytes of the message + length of the secret

# following the MD4 RFC 1320 padding
def make_padding(length):
    tmp = [0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
           0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
           0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
           0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    if length < 56:
        padding = tmp[0:(56-length % 64)]
    else:
        padding = tmp[0:(64+56-len % 64)]
    length = length << 3
    for i in range(8):
        padding.append((length >> (8*i)) % 256)

    return padding


padding = make_padding(length_initial)
padding = [hex(x)[2:] for x in padding]
final_padding = ""
for x in padding:
    if len(x) == 1:
        x = "0" + x
    final_padding += x
bytes_message += bytes.fromhex(final_padding)
bytes_message += bytes(";verified=true", "utf-8")
print(bytes_message.hex())

#output the forged message