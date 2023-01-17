# Wireshark doo dooo do doo...

## Problem Statement

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/ea41c400c3c7b4a63406e5e607d362ab/shark1.pcapng).

## Type

Forensics

## Hints

None

## Approach
1. Learned how to use wireshark.
2. In wireshark I searched `tcp contains pico` but got nothing :/
3. Used wireshark to open the file, checked the protocol heirarchy and filtered the line based text data, followed the tcp stream and got encrypted flag  `Gur synt vf cvpbPGS{c33xno00_1_f33_h_qrnqorrs}`
on comparing this to `picoCTF` we can see that c -> p & p-> c, so this is symmetrical hence, rot13. On applying rot13 to this text we get our flag.

## Flag

The flag is picoCTF{p33kab00_1_s33_u_deadbeef}