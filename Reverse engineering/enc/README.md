
# Transformation

## Problem description
 
 I wonder what this really is...[enc](https://mercury.picoctf.net/static/2b4cea9b07db22bf4f933fddd1b8caa9/enc)
  ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
## Type 
 Reverse engineering

 ## Hints

1. You may find some decoders online

## Approach

 Text given: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽

and a python snippet is given with functions chr() and ord() 

- The Python ord() function is used to convert a single Unicode character into its integer representation. We can pass in any single string character and the function will return an integer.

- The Python chr function does the opposite of the ord function: it converts an integer representation into its corresponding Unicode string character. 

On analysing the python code we can see that the function is parsing through each flag character.
So, the given text is our encoded flag. 

Reversing the code:

As our encoded is the combination of 2 functions we'll print the decoded flag for both the functions simultaneously

    print(chr(ord(encoded_string[i])>>8),end='')
    print(chr((ord(encoded_string[i]))-((ord(encoded_string[i])>>8)<<8)),end='')

    # end='' to print our flag in a single line

and we have our flag: 

picoCTF{16_bits_inst34d_of_8_04c0760d}