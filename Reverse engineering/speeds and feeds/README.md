# speeds and feeds

## Problem Statement

There is something on my shop network running at nc mercury.picoctf.net 7032, 
but I can't tell what it is. Can you?

## Type

Reverse Engineering

## Hints

1. What language does a CNC machine use?

## Approach

When connected to the given service we get a list of commands written in G-CODE.
Using an online g-code simulator [tool](https://nraynaud.github.io/webgcode/) to map the code and we get our flag. 

## Flag

picoCTF{num3r1cal_c0ntr0l_a067637b}