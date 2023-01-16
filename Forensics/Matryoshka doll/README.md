# Matryoshka doll

## Problem Statement

Matryoshka dolls are a set of wooden dolls of decreasing size 
placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5ef2e9103d55972d975437f68175b9ab/dolls.jpg)


## Type

Forensics

## Hints

1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

## Approach

Zip files can be hidden inside JPGs, so I kept changing the file type and extracting it till I got the flag file.
## Flag

picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}