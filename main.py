"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time

from angry import Angry
from smiley import Smiley
from sense_hat import SenseHat


def main():
    #smiley = Sad(complexion=Smiley.BLUE)
    #smiley =  Happy(complexion=Smiley.RED)
    smiley = Angry()

    smiley.show()

    time.sleep(1)

    smiley.blink()

if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

