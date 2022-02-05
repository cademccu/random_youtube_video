#! /usr/bin/env python3

import sys
import subprocess
import requests
import random
import string

# https://webapps.stackexchange.com/questions/54443/format-for-id-of-youtube-video



def main():
    _PREFIX = "https://www.youtube.com/watch?v="
    # https://www.youtube.com/watch?v=jflXUguoKtU
    _LENGTH = 11
    #pattern = "This video isn't available anymore"
    pattern = "Video unavailable"
    
    ID = ""
    search_string = string.ascii_letters + string.digits
    search_string += "-_"
    n = len(search_string)

    COUNT = 0
    while True:
        for i in range(_LENGTH):
            ID += search_string[random.randrange(n)]

        URL = _PREFIX + ID
        #URL = "https://www.youtube.com/watch?v=tzZV0W5Eu7c"
        result = requests.get(URL)
        print(URL)
        COUNT += 1
        #l = result.text.split("\n")
        #print(l[20])


        if pattern not in result.text:
            with open("output.txt", "w") as output:
                output.write(result.text)
                print("COUNT: " + str(COUNT))
            print("BREAKING")
            break
        ID = ""
    


if __name__ == "__main__":
    main()
