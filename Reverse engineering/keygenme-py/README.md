# keygenme_py

## Problem statement

[keygenme_trial.py](https://mercury.picoctf.net/static/a6d9cac3bfa4935ceb50c145d3ff5586/keygenme-trial.py)

## Type

Reverse engineering

## Hints

none

## Approach

aight for this one we just have a python file, so we go ahead and open it in a code editor.
On running the code, we get
```
Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, PRITCHARD (a/b/c/d)?
```
on selecting option (b) we get the reply

```
You must buy the full version of this software to use this feature!
```
so from this we deduct that we need the license key.

from the file we find that we have part of the flag provided
```
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
```
so we know that our flags looks like
```
picoCTF{1n_7h3_|<3y_of_xxxxxxxx}
```

2nd part of flag is static, so it means some function is changing its value
on scrollign down, we find 2 functions working on license key

```
def enter_license():
    if check_key(user_key, bUsername_trial):

def check_key(key, username_trial):
    if key[i] != hashlib.sha256(username_trial).hexdigest()[n]:
```

enter_license() function takes in user input as user_key and a predefined string value bUsername_trial and passes ti on to another function

check_key()

notice that in dynamic part of our key, it's length is 8 and we have ckeck_key[i] function checking the hashed output for 8 values only.
Hence, those 8 specific values from the hash is our static key/flag.
Input for hash function is bUsername_trial.

Here,

bUsername_trial = b"PRITCHARD"  

is given in the script. Now, we oprn up our terminal and import hashlib


## Terminal

![terminal picture](https://i.imgur.com/Qb3GP3f.png)

so our static key is,

54ef6292

## Flag

picoCTF{1n_7h3_|<3y_of_54ef6292}

