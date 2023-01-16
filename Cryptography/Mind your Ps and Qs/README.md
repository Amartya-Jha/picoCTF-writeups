# 13

## Problem Statement

In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](https://mercury.picoctf.net/static/51d68e61bb41207a55f24e753f07c5a3/values)

## Type

Cryptography

## Hints

1. Bits are expensive, I used only a little bit over 100 to save money

## Approach

we use an online [tool](https://www.dcode.fr/rsa-cipher) to decrypt the text and we get our flag.

## Flag

picoCTF{sma11_N_n0_g0od_05012767}