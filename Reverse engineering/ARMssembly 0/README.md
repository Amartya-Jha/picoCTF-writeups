# ARMssembly 0

## Problem Statement

What integer does this program print with arguments 1765227561 and 1830628817? 
File: [chall.S](https://mercury.picoctf.net/static/37069d9462289016ea1869ef4c993912/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})


## Type

Reverse Engineering

## Hints

1. Simple compare

## Approach

```
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
```
```sp: stack pointer
sub: subtraction
str: store
ldr: load
cmp: compare
bls: branch if less
```

we are storing the input values in w0 and w1 on sp stack.
Then we are loading w0 in w1 and w1 in w0, and comparing.
if less w0 is smaller than w1, we branch to L2.

```
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
```
In L2 input stored at 8th position is loaded to w0 and fed into func1.

In L3 16 is added to sp.

So our flag should be the greater of the 2 inputs converted to hex.
## Flag

picoCTF{6d1d2dd1}