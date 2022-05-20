#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dictionary = a_dictionary.copy()
    for i in my_dictionary:
        my_dictionary[i] = my_dictionary[i] * 2
    return my_dictionary
