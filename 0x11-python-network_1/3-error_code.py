#!/usr/bin/python3
"""
    Script that send a POST request to the passed URL
    Return the body of the response.
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as body:
            print(body.read().decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))


# encode: when the result contains "str" data ==> "bytes" data
# decode: when the result contains "bytes" data ==> "str" data
