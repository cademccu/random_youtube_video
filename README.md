# random_youtube_video
Method(s) to get random youtube videos


### PRECONDITIONS

YouTube video URL's take the form of:
```
https://www.youtube.com/watch?v=###########
```
where "###########" represents the 11 digit video ID. The characters in the 
ID string can be:
```
[A-Z] | [a-z] | [0-9] | [_-]
```
Which totals 64 total possible options for each letter and 64^11 permutations.
This makes it almost impossible to truly randomly generate a URL, since that
space is nowhere near occupied with videos. Hence some of the methods here to generate
some kind of pseudorandomness.


### bruteForce.py
This is the basic method for brute forcing a random URL. Takes the space of 64^11 and
uses python3's random module to select from that set, then ask youtube if that video 
exists. Since the likelyhood of a hit is so low, this looks like a DOS of youtube's 
servers more than anything. A first attempt for proof of concept, before I remembered
my equations from my discrete mathematics class.

### randomSearch.py
This is a slightly better method for randomness, generates a random string of characters
from the set 
```
[A-Za-z]
```
of length provided by the first argument:
```
python3 randomSearch.py <STRING_LENGTH>
```
String length defaults to 5 if no arg given, seems to give a consistant amount of results.

The search is then done by searching youtube for the randomly generated string, getting
a random video ID from the results returned (if more than 1) and writing the full URL
to stdout.

TODO: Add webdriver support?







