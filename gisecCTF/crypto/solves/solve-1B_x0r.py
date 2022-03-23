from pwn import xor
from random import randbytes

cipher = b'\xdd\xf3\xe9\xff\xf9\xd9\xce\xdc\xe1\xf5\xf4\xff\xc5\xf8\xe3\xee\xff\xc5\xe2\xf5\xe8\xc5\xf3\xe9\xc5\xe9\xf5\xc5\xff\xfb\xe9\xe3\xc5\xff\xec\xff\xf4\xc5\xf3\xfc\xc5\xee\xf2\xff\xc5\xf1\xff\xe3\xc5\xf3\xe9\xc5\xe8\xfb\xf4\xfe\xf5\xf7\xe7'

while True:
    flag = xor(cipher, randbytes(1))
    if b'CTF' in flag:
        print(flag)
        break

# Flag : GisecCTF{one_byte_xor_is_so_easy_even_if_the_key_is_random}

