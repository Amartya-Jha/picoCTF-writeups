# MacroHard WeakEdge

## Problem Statement

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/c0da20f29337e87ffb58ea987d8c596e/Forensics%20is%20fun.pptm)

## Type

Forensics

## Hints

None

## Approach

Google how to hide data inside ppts and found out most ms office things can be unzipped???

Got the file in my linux machine using 
`wget https://mercury.picoctf.net/static/c0da20f29337e87ffb58ea987d8c596e/Forensics%20is%20fun.pptm`

then, `unzip Foresics is fun.pptm`

In the unzipped files I see a hidden file name ![hidden](https://i.imgur.com/7GLu2Wo.png) 
on opening the hidden file using `cat ppt/slideMasters/hidden` we get the following text

`Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f` which seems to be base64 encoded, we need to decode and remove the spaces to retrieve our flag, which I did using the following command

`cat hidden | sed 's/ //g' | base64 -d` and we got our flag.

## Flag

picoCTF{D1d_u_kn0w_ppts_r_z1p5}