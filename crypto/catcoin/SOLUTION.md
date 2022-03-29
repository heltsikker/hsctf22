The intended way to solve this challenge is to realize that if you get two different third messages, both of which use the same *r*, then it's an easy task to compute *x*: Simply ask for the third message with *e=1 (z1 = r + x)* and *e=0 (z2 = r)*. Then *z1-z2 = x*. And there is nothing in Alice's implementation which blocks this simple attack. In fact, in this implementation, Alice has chosen a single value for *r* which she will use for all proofs (both the first and third messages). So you might get wind of this strategy if you ask for new first messages: You will get the same *a* over and over again.

It might also be possible to break the discrete logarithm directly, but probably not, as *p* is a 2048-bit safe prime. (But I have not done anything special to check that this cannot be done)

Some background:
Schnorr's protocol is a serious cryptographic protocol, and variants of it are in use in various settings, and other protocols of a similar nature are used in Bitcoin and various cryptocurrencies to prove that transactions were done correctly.

Schnorr's protocol is secure if you ensure that
1) You always use fresh randomness when generating the first message.
2) You ensure that you never use the same *r* when computing the third message.
3) Plus some other annoying cryptographic details. (You should probably not implement it yourself unless you are aware of all of them.)

In practice, you can easily make this into a non-interactive proof by computing the second message as a hash of the first message, and then Alice could simply publish the entire proof at once without having to interact with everyone who wanted to verify it.

Side note: There is actually a cryptocurrency called CatCoin, which does not to my knowledge work anything like what is described here.
