#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    r = number % (-10)
else:
    r = number % 10

if r > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, r))
elif r == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, r))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, r))
