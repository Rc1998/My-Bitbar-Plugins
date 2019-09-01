#!/usr/local/bin/python3

# BitBar plugin for random ambient soundtracks from '/Users/ryancampbell/Documents/ambient'
import os, glob, sys
from random import randint 

dir = '/Users/ryancampbell/Documents/ambient'
files = glob.glob(os.path.join(dir, '*.mp4'))

print('Ambient')
print('---')
# print('Shuffle | terminal=true bash=/usr/bin/open param1={0}'.format(files[y]))

def playRandomSong():
    y = randint(0, len(files) - 1)
    os.system('/usr/bin/open {}'.format(files[y]))


if len(sys.argv) == 1:
    print('Shuffle | refresh=true terminal=false bash="/usr/local/bin/python3" param1="/Users/ryancampbell/BitBar/ambient.30m.py" param2=play')
else: 
    playRandomSong()

