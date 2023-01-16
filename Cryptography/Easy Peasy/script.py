from pwn import *

encTxt = bytes.fromhex("03463d190702003d195004133d190356433d1902503d1950563d1900513d1959")
encFlag = bytes.fromhex("51466d4e5f575538195551416e4f5300413f1b5008684d5504384157046e4959")
decTxt = b'a'*32

key = xor(encTxt, decTxt)

print(xor(encFlag, key).decode())