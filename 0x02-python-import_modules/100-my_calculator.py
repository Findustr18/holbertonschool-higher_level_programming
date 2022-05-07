#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <a>")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    op = argv[2]
    dict_math = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in dict_math:
        print("Unknow operator. Available operators: +, -, *, /")
        exit(1)
    print("{:d} {} {:d} = {:d}".format(a, op, b, dict_math[op](a, b)))
