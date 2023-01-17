# tunn3l v1s10n

## Problem Statement

We found this [file](https://mercury.picoctf.net/static/da18eed3d15fd04f7b076bdcecf15b27/tunn3l_v1s10n). Recover the flag.

## Type

Forensics

## Hints

1. Weird that it won't display right...

## Approach

We open the given file in a hex editor and see that its a bitmap file, on changing the file type to .bmp, it was still corrupted.
So I took a sample bmp image and compared the values to our file and saw there's 2 "BA D0" values which are faulty and fixd them accordingly.

![image](https://i.imgur.com/ZxYPwuV.png)

and we get this image which is not very helpful.

![size](https://i.imgur.com/jiLfHN7.png)

The name of the challenge is tunnel vision so i thought maybe we need to zoom out a bit and checked the dimensions of the image. 
The height was 334 pixels which was a bit odd so i checked its hex value which is 0x14E or 4E 01 in little endian, and looked for those values in the hex editor and changed it to 830 pixels (hit and try) or 3E 03 in hex values and we get our flag.

![flag](https://i.imgur.com/Bo1ZBkv.png)


## Flag

picoCTF{qu1t3_a_v13w_2020}