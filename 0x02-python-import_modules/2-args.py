#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    p = len(argv)
    print("{:d} {:s}{:s}".format(p - 1, "argument" if p <= 2 else "arguments",
                                 "." if p == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
