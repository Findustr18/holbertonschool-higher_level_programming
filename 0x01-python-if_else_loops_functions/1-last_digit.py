#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = -((-1 * number) % 10)
else:
    n = number % 10
if n > 5:
    print(f'Last digit of {number} is {n} and is greater than 5\n')
elif n == 0:
    print(f'Last digit of {number} is {n} and is 0\n')
else:
    print(f'Last digit of {number} is {n} and is less than 6 and not 0\n')
