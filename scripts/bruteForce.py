#! /usr/bin/env python3

import sys
import requests
import random
import string

# https://webapps.stackexchange.com/questions/54443/format-for-id-of-youtube-video



def main():

    # Check lol
    resp = input("""[WARN]  This function searches for a random youtube video by randomly
           generating URLs, of which the are 64^11 possible URLs and a mere
           14 Billion (or slightly north of that) existing videos. The chance
           of any one URL being valid is: 

                1.8973538018496328e-10

           So.... don't count on this working. It doesn't work fast enough as 
           it has to make a request to youtube, and parse the response to
           figure out if the video exists -- which takes awhile. I would need
           to find a way to make _at_minimum_ thousands of requests a second
           (which youtube probably wouldn't appreciate) to even have a chance.
           So this just stays around for novelty reasons.

           That being said... are you sure you want to run this program?

Continue? [Y/n]:  """)
    if resp not in ["y", "Y", "yes", "Yes"]:
        print("\nGood call! Try some of the other scripts.\nExiting...\n")
        sys.exit(0)

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
    pattern = "This video isn't available anymore"
    
    ID = ""
    URL = ""

    search_string = string.ascii_letters + string.digits
    search_string += "-_"
    n = len(search_string)

    COUNT = 0
    try:
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
    except KeyboardInterrupt:
        print("\n[INFO] Program finished...\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
