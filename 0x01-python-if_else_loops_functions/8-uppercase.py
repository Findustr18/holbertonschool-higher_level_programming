#!/usr/bin/python3
def uppercase(str):
    for x in str:
        n = ord(x)
        if (n > 96) and (n < 123):
            n = n - 32
        print("{:s}".format(chr(n)), end="")
    print("")
