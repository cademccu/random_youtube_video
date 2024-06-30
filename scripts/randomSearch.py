import urllib.request
import re
import random
import string
import sys


def getSearchString(length):
    query = ""
    for i in range(length):
        query += string.ascii_letters[random.randrange(len(string.ascii_letters))]
    return query

def getVideoList(query):
    search_string = "https://www.youtube.com/results?search_query=" + query
    html = urllib.request.urlopen(search_string).read().decode()
    video_ids = re.findall(r"watch\?v=(\S{11})", html)
    if len(video_ids) < 1:
        return None

    return "https://www.youtube.com/watch?v=" + video_ids[random.randrange(len(video_ids))]

def main():
    DEFAULT_LENGTH = 5
    if len(sys.argv) == 2:
        DEFAULT_LENGTH = int(sys.argv[1])
    while True:
        query = getSearchString(DEFAULT_LENGTH)
        print("SEARCH STRING: " + query)
        URL = getVideoList(query)
        if URL is not None:
            ######################################################################
            # This would be where I could use a chromedriver or open the webpage
            # in something to be extra quirky.
            ######################################################################
            print("Random URL: \n" + URL)
            break

    return 0


if __name__ == "__main__":
    main()
