# Information

## Problem Statement

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg)
![cat](https://i.imgur.com/tljYe3I.jpg)

## Type

Reverse Engineering

## Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

## Approach

Used an online [tool](https://exif.tools/upload.php) to check the exif metadata of the file and saw this 
![license](https://i.imgur.com/ChBsvwV.png), which looks like a base64 encoded string, on decoding this we get our flag.
## Flag

picoCTF{the_m3tadata_1s_modified}