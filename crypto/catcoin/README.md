Category: crypto
Title: CatCoin
Author: Arne Tobias Ødegaard @ SimulaUiB
Description:
Alice has started using the newest cryptocurrency CatCoin.
An account in CatCoin consists a private key, known only to the owner, and a public key, known to the public.
She has a private key, an integer *x* modulo *p-1*.
Alice has taken a private password, transformed each character into a binary string by using the **7-bit** ASCII table, and concatenated all the bits to form her private key. Your job is to find Alice's private password.
Her public key is *h = 2^x^* modulo *p*, and is given in the attached file `public_key.txt`.
*p* is a fixed parameter of CatCoin, and is given in the attached file `p.txt`.

Alice wants to prove to other people that she owns her account, i.e. knows her private key. For this purpose, she wants to use a Schnorr protocol to prove that she knows the discrete logarithm of her public key. The protocol goes as follows: Alice picks a random *r* modulo *p-1*, and computes *a = 2^r^* modulo *p*, and sends this to Bob, who wants to verify her claim. Bob picks a random integer *e* modulo *p-1* and sends it to Alice. Alice responds with *z = r + ex* modulo *p-1*. Bob can then verify whether *2^z^ = ah^e^* modulo *p*, in which case he can be convinced that Alice is the owner of the account.

For the purposes of this, Alice has set up a web service at `catcoin.heltsikker.no` on port `7001`. You can interact with the web service as follows:
* Send the command `1`, after which you get *a = 2^r^* modulo *p* for some *r*.
* Send the command `3 a e`, in which you get the integer *z = r + ex* modulo *p-1*, as long as *a* is a previous message sent by Alice, and *e* is an integer from *0* to *p-1*.

Simula UiB driver forskning og utdanning innen datasikkerhet med fokus på informasjonsteori og kryptologi. Selskapet ansetter alt fra Summer interns til PhD-stipendiater og seniorforskere. Interessert i en forskningsutdanning? Sjekk ut https://simula-uib.com/.

Flag: HSCTF{Schnorr_rest_for_the_wicked}

Difficulty: Medium
