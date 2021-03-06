#!/usr/bin/python2.7

# Implementation of RIPEMD160 taken 
# from https://github.com/jcook/python-crypto-debian/blob/master/lib/Crypto/Hash/RIPEMD160.py
# with some adaptation


import struct

# ATTACK: mac given in the challenge and length of the first block in bytes
mac = "50cb15dc7c9eac0d5532d78f3622c73d4369d803"
initial_length = 64

def u32(n):
    return n & 0xFFFFffff

#
# Ordering of the message words
#

# The permutation rho
rho = [7, 4, 13, 1, 10, 6, 15, 3, 12, 0, 9, 5, 2, 14, 11, 8]

# The permutation pi(i) = 9i + 5  (mod 16)
pi = [(9*i + 5) & 15 for i in range(16)]

# Round permutation r (left line)
rl = [range(16)]                    # id
rl += [[rho[j] for j in rl[-1]]]    # rho
rl += [[rho[j] for j in rl[-1]]]    # rho^2
rl += [[rho[j] for j in rl[-1]]]    # rho^3
rl += [[rho[j] for j in rl[-1]]]    # rho^4

# r' (right line)
rr = [list(pi)]                     # pi
rr += [[rho[j] for j in rr[-1]]]    # rhopi
rr += [[rho[j] for j in rr[-1]]]    # rho^2 pi
rr += [[rho[j] for j in rr[-1]]]    # rho^3 pi
rr += [[rho[j] for j in rr[-1]]]    # rho^4 pi

#
# Boolean functions
#

# f (x, y, z) = x ^ y ^ z
f1 = lambda x, y, z: x ^ y ^ z

# f (x, y, z) = (x ^ y) v (!x ^ z)
f2 = lambda x, y, z: (x & y) | (~x & z)

# f (x, y, z) = (x v !y) ^ z
f3 = lambda x, y, z: (x | ~y) ^ z

# f (x, y, z) = (x ^ z) v (y ^ !z)
f4 = lambda x, y, z: (x & z) | (y & ~z)

# f (x, y, z) = x ^ (y v !z)
f5 = lambda x, y, z: x ^ (y | ~z)

# boolean functions (left line)
fl = [f1, f2, f3, f4, f5]

# boolean functions (right line)
fr = [f5, f4, f3, f2, f1]

#
# Shifts
#

# round   X0  X1  X2  X3 ...
_shift1 = [11, 14, 15, 12, 5, 8, 7, 9, 11, 13, 14, 15, 6, 7, 9, 8]
_shift2 = [12, 13, 11, 15, 6, 9, 9, 7, 12, 15, 11, 13, 7, 8, 7, 7]
_shift3 = [13, 15, 14, 11, 7, 7, 6, 8, 13, 14, 13, 12, 5, 5, 6, 9]
_shift4 = [14, 11, 12, 14, 8, 6, 5, 5, 15, 12, 15, 14, 9, 9, 8, 6]
_shift5 = [15, 12, 13, 13, 9, 5, 8, 6, 14, 11, 12, 11, 8, 6, 5, 5]

# shifts (left line)
sl = [[_shift1[rl[0][i]] for i in range(16)]]
sl.append([_shift2[rl[1][i]] for i in range(16)])
sl.append([_shift3[rl[2][i]] for i in range(16)])
sl.append([_shift4[rl[3][i]] for i in range(16)])
sl.append([_shift5[rl[4][i]] for i in range(16)])

# shifts (right line)
sr = [[_shift1[rr[0][i]] for i in range(16)]]
sr.append([_shift2[rr[1][i]] for i in range(16)])
sr.append([_shift3[rr[2][i]] for i in range(16)])
sr.append([_shift4[rr[3][i]] for i in range(16)])
sr.append([_shift5[rr[4][i]] for i in range(16)])

#
# Constants
#

_kg = lambda x, y: int(2**30 * (y ** (1.0 / x)))

# constants (left line)
KL = [
    0,          # Round 1: 0
    _kg(2, 2),  # Round 2: 2**30 * sqrt(2)
    _kg(2, 3),  # Round 3: 2**30 * sqrt(3)
    _kg(2, 5),  # Round 4: 2**30 * sqrt(5)
    _kg(2, 7),  # Round 5: 2**30 * sqrt(7)
]

# constants (right line)
KR = [
    _kg(3, 2),  # Round 1: 2**30 * cubert(2)
    _kg(3, 3),  # Round 2: 2**30 * cubert(3)
    _kg(3, 5),  # Round 3: 2**30 * cubert(5)
    _kg(3, 7),  # Round 4: 2**30 * cubert(7)
    0,          # Round 5: 0
]

# cyclic rotate
def rol(s, n):
    assert 0 <= s <= 31
    assert 0 <= n <= 0xFFFFffff
    return u32((n << s) | (n >> (32-s)))

# Initial value, ATTACK: initialized to the mac
initial_h = tuple(struct.unpack("<5L", mac.decode('hex')))

def box(h, f, k, x, r, s):
    assert len(s) == 16
    assert len(x) == 16
    assert len(r) == 16
    (a, b, c, d, e) = h
    for word in range(16):
        T = u32(a + f(b, c, d) + x[r[word]] + k)
        T = u32(rol(s[word], T) + e)
        (b, c, d, e, a) = (T, b, rol(10, c), d, e)
    return (a, b, c, d, e)

def _compress(h, x):    # x is a list of 16 x 32-bit words
    hl = hr = h

    # Iterate through all 5 rounds of the compression function for each parallel pipeline
    for round in range(5):
        # left line
        hl = box(hl, fl[round], KL[round], x, rl[round], sl[round])
        # right line
        hr = box(hr, fr[round], KR[round], x, rr[round], sr[round])

    # Mix the two pipelines together
    h = (u32(h[1] + hl[2] + hr[3]),
         u32(h[2] + hl[3] + hr[4]),
         u32(h[3] + hl[4] + hr[0]),
         u32(h[4] + hl[0] + hr[1]),
         u32(h[0] + hl[1] + hr[2]))

    return h

def compress(h, s):
    """The RIPEMD-160 compression function"""
    assert len(s) % 64 == 0
    p = 0
    while p < len(s):
        h = _compress(h, struct.unpack("<16L", s[p:p+64]))
        p += 64
    assert p == len(s)
    return h

digest_size = 20

def update(data,ripe_h,ripe_bytes,ripe_buf):
    ripe_buf += data
    ripe_bytes += len(data)
    p = len(ripe_buf) & ~63     # p = floor(len(ripe_buf) / 64) * 64
    if p > 0:
        ripe_h = compress(ripe_h, ripe_buf[:p])
        ripe_buf = ripe_buf[p:]
    assert len(ripe_buf) < 64
    return (ripe_h,ripe_bytes,ripe_buf)

def digest(ripe_h,ripe_bytes,ripe_buf):
    # Merkle-Damgard strengthening, per RFC 1320
    # We pad the input with a 1, followed by zeros, followed by the 64-bit
    # length of the message in bits, modulo 2**64.
    # ATTACK: WE ADD 64 the length of the first block which is now part of our message
    length = ((ripe_bytes + initial_length) << 3) & (2**64-1) # The total length of the message in bits, modulo 2**64
    assert len(ripe_buf) < 64
    data = ripe_buf + "\x80"
    if len(data) <= 56:
        # one final block
        assert len(data) <= 56
        data = struct.pack("<56sQ", data, length)
    else:
        assert len(data) <= 120
        data = struct.pack("<120sQ", data, length)
    h = compress(ripe_h, data)
    return struct.pack("<5L", *h)

def hexdigest(ripe_h,ripe_bytes,ripe_buf):
    return digest(ripe_h,ripe_bytes,ripe_buf).encode('hex')

#string to add to the new message
message = ";verified=true"
ripe_h = initial_h
ripe_bytes = 0
ripe_buf = ""

(ripe_h,ripe_bytes,ripe_buf) = update(message,ripe_h,ripe_bytes,ripe_buf)
print(hexdigest(ripe_h,ripe_bytes,ripe_buf))

