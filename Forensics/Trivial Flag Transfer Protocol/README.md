# Trivial Flag Transfer Protocol

## Problem Statement

Figure out how they moved the [flag](https://mercury.picoctf.net/static/4fe0f4357f7458c6892af394426eab55/tftp.pcapng).

## Type

Forensics

## Hints

1. What are some other ways to hide data?

## Approach

On opening the given file with wireshark, we extract TFTP objects and get the following objects 

![objects](https://i.imgur.com/z5G97po.png)

we save the files and head to the `instructions.txt` file which contains `GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA` which looks like a substituion cipher. Decoding this with ROT13, we get `TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN`. So now we check the plan file which contains another encrypted string
`VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF` which on decrypting gives us `IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS`

## Flag

picoCTF{D1d_u_kn0w_ppts_r_z1p5}