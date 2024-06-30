


###########################################################################
# The purpose of this file is to collect different methods of randomness
# that can be plugged in/exchanged.
#
# They should follow the same format, so they can be used interchangably.
# The format I am selecting for this program is that of random.randrange()
# without the need for a step variable as this functionality likely isn't
# needed in practice here.
###########################################################################

import random
import sys

def RANDOM_TEMPLATE(n, stop=None):
    start = 0 if stop is None else n
    stop = n if stop is None else stop

    # do whatever it is you do for randomness

    return None # return value!
        



def RANDOM_randrange(n, stop=None):
    start = 0 if stop is None else n
    stop = n if stop is None else stop

    return random.randrange(start, stop)
