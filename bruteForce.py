#! /usr/bin/env python3

import sys
import requests
import random
import string

# https://webapps.stackexchange.com/questions/54443/format-for-id-of-youtube-video



def main():
    ###################################################
    # This function assumes (most) youtube URLs are 11
    # char strings consisting of a-zA-Z0-9_- (64 total)
    # and generates them randomly, logging every URL to
    # std out. Every URL is checked via request to see
    # if it is a valid URL, if so the program finishes
    # with a COUNT and final successful URL. Time 
    # complexity of this is FOREVER so thus brute
    # force.
    ###################################################
    _PREFIX = "https://www.youtube.com/watch?v="
    _LENGTH = 11
    pattern = "Video unavailable"
    
    ID = ""
    URL = ""

    search_string = string.ascii_letters + string.digits
    search_string += "-_"
    n = len(search_string)

    COUNT = 0
    while True:
        for i in range(_LENGTH):
            ID += search_string[random.randrange(n)]

        URL = _PREFIX + ID
        result = requests.get(URL)
        print(URL)
        COUNT += 1

        if pattern not in result.text:
            print("COUNT: " + str(COUNT))
            print("FINAL URL: " +  URL )
            break
        ID = ""


if __name__ == "__main__":
    main()
