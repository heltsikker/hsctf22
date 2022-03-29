from gmpy2 import isqrt
import time

# Perform Fermat attack on RSA parameter N=p*q, returns p, q.
def FermatAttack(n):
	a = b = isqrt(n)
	b2 = pow(a,2)-n
	while pow(b,2)!=b2:
		a += 1
		b2 = pow(a,2)-n
		b = isqrt(b2)
	return a+b, a-b

# ASCII encode
# s: string to be converted to list of integers based on ASCII table.
def ascii_encode(s):
	return [ord(i) for i in list(s)]

# ASCII decode
# s: list of integers based on ASCII table to be converted to string.
def ascii_decode(x):
	return ''.join([chr(i) for i in x])

# RSA encrypt
# Input the message (as string) and public key, return ciphertext represented as
# list of integers mod N.
def rsa_enc(msg, N, e):
	return [pow(i,e,N) for i in ascii_encode(msg)]

# RSA decrypt
# Input the ciphertext as list of integers mod N, public value N and private
# exponent d, return message (as string).
def rsa_dec(c, N, d):
	return ascii_decode([pow(i,d,N) for i in c])

# Message to encrypt.
msg = "T"

# Difficulty, from 0 (= easiest), to 4 (= hardest).
# difficulty = 0: 20 bits
# difficulty = 1: 40 bits
# difficulty = 2: 2048 bits
# difficulty = 3: 2048 bits
# difficulty = 4: 2048 bits
difficulty = 2

# Attack
run_attack = False
# Time to run the attack.
# Resources: Intel Core i5-8250U, Windows 10, Python 3.10.3.
# difficulty = 0: 0s
# difficulty = 1: 0s
# difficulty = 2: 0s
# difficulty = 3: 12s
# difficulty = 4: 50s

priv_keys = []
# 2^10 * 2^10 = 2^20
priv_keys.append([1031,1021])

# 2^20 * 2^20 = 2^40
priv_keys.append([1048583,1048573])

# 2^1024 +/- 2^450
priv_keys.append([
	179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865488183657116783673656316748314504103143183403593431614704007434709833097979690755043815448789153294209488988566141369547090468030738594777,
	179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865482368947322418818531922157851400066868354272707933070221755513116387983674783571657205920383443185685002888393291240123622191217709677351
])

# 2^1024 +/- 2^524
priv_keys.append([
	179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639529042759048938302585340482694870746984249601854229395360161476511635027809644129890893587666118873603168881175718145104244221842477449455335948555953144594021,
	179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639419205996486848547145630069909568455507938637051936508809850061164666336875281633056932633415535600723532140193454451375650270034481983154334764103295303679789
])

# 2^1024 +/- 2^525
priv_keys.append([
	179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639583961140329983180305195689087521892722405084255375838635317184185119373276825378307874064791410510042987251666849991968541197746475182605836540782282065049879,
	179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639364287615205803669425774863516917309769783154650790065534694353491181991408100384639952156290243964283713769702322604511353294130484250003834171876966383221991
])

# RSA
start_time = time.time()
p, q = priv_keys[difficulty]
N = p*q
phi_n = (p-1)*(q-1)
e = pow(2,16)+1
d = pow(e, -1, phi_n)
c = rsa_enc(msg, N, e)
recovered_msg = rsa_dec(c, N, d)
end_time = time.time()

print(f"\nPrivate key:\np = {p}\nq = {q}\nd = {d}")
print(f"\nPublic key:\nN = {N}\ne = {e}")
print(f"\nMessage: {msg}.")
print(f"Encoded message: {ascii_encode(msg)}.")
print(f"\nEncoded ciphertext: {c}.")
print(f"\nRecovered message: {recovered_msg}.")
print(f"\nRSA functionality test passed: {msg==recovered_msg}.")
print(f"RSA execution time: {end_time-start_time:.3f} seconds.")

# Attack
if run_attack:
	start_time = time.time()
	computed_factors = FermatAttack(N)
	end_time = time.time()
	print(f"\nAttack successful: {p==computed_factors[0] and q==computed_factors[1]}.")
	print(f"Attack execution time: {end_time-start_time:.3f} seconds.")
	if p!=computed_factors[0] or q!=computed_factors[1]:
		print(f"p': {computed_factors[0]}")
		print(f"q': {computed_factors[1]}")
