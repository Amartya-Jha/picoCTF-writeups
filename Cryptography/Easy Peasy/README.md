# Easy Peasy

## Problem Statement

A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) nc mercury.picoctf.net 64260 [otp.py](https://mercury.picoctf.net/static/338fdafc11b7fbfb9cca5edac5085d05/otp.py)

## Type

Cryptography

## Hints

1. Maybe there's a way to make this a 2x pad.
## Approach

when connected to the terminal we get the following
![image](https://i.imgur.com/khav0TF.png)

from the given python file we can see that the xor file pads the input with the same key after every 50000 character so if we get our input encrypted with the same xor value. then we can xor the input with enc result and get the key.

Then XORing the key with encrypted flag we should get the decoded flag.

By running the follwing cmd we get our enc text padded with the same xor values as the encrypted flag
```
python -c "print('a'*49968); print('a'*32)" | nc mercury.picoctf.net 64260
```

#### Running the following script we get the flag

```http
from pwn import *

encTxt = bytes.fromhex("03463d190702003d195004133d190356433d1902503d1950563d1900513d1959")
encFlag = bytes.fromhex("51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959")
decTxt = b'a'*32

key = xor(encTxt, decTxt)

print(xor(encFlag, key).decode())
```

## Flag

picoCTF{3a16944dad432717ccc3945d3d96421a}