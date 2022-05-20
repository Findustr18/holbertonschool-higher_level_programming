#!/usr/bin/python3
def roman_to_int(roman_string):
    mapper = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result = 0

    for idx in range(0, len(roman_string)):
        if idx == len(roman_string) - 1:
            result += mapper[roman_string[idx]]
            break

        if mapper[roman_string[idx]] < mapper[roman_string[idx + 1]]:
            result -= mapper[roman_string[idx]]
        else:
            result += mapper[roman_string[idx]]

    return result
