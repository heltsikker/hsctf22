# Bradley Urglar's API

Signy Odding is writing her PhD on the history of hacking, and came across the classical works of Bradley Urglar, famous hacker and technology wizard.

Rumour has it that Bradley created the Holy Grail of APIs. Unfortunately, Signy has yet to figure out a way to access it with her old account from back in the day.

Can you help Signy dig up the historical treasures of Bradley Urglar?

## Task

Log in to Bradley's community site as Signy and uncover out the secrets of the ancient API.
* URL: https://b-urglar-ctf.labs.nais.io
* Username: `greenemerald`
* Password: `farmer3`

## Hints
1. The top entry on [OWASP top 10](https://owasp.org/www-project-top-ten/) for 2021 is a good place to start reading
2. Bradley claims the user database is slightly corrupted, but are _all_ users corrupted? How can you find out, without logging in as other users?

---

## Technical

By Jan-Kåre Solbakken & Julian Ravn Thrap-Meyer @ NAV IT 

* Category: `web`
* Difficulty: `easy`
* Flag: `HSCTF{Brad1337IsTooCoolForSchool}`

### Running on a non-[nais](https://nais.io) infrastructure:

1. Build the app Dockerfile
2. Run the container with the `PORT` environment variable with your desired port (default is 3000).
3. Remember to update the README and SOLUTION with the correct URLs :-)
