#!/Users/ryancampbell/python/.venv/bitbar/bin/python

from os import system
import sys
from AppKit import NSScreen

toggleRegularRes = '/usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:2560x1440 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"'
toggleGameRes = '/usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:1920x1080 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"'

screenHeight = NSScreen.mainScreen().frame().size.height

def toggle():
    if screenHeight == 1440:
        system(toggleGameRes)
    else:
        system(toggleRegularRes)

if len(sys.argv) == 1:
    print('{} | refresh=true terminal=false bash="/Users/ryancampbell/python/.venv/bitbar/bin/python" param1="/Users/ryancampbell/BitBar/resToggle.py" param2=toggle'.format(int(screenHeight)))
else: 
    toggle()

'''
if len(sys.argv) == 1:
    print('{}x{} | refresh=true'.format(int(screenWidth), int(screenHeight)))
    print('---')
    print('2560 | terminal=false bash="/usr/local/bin/python3" param1="/Users/ryancampbell/BitBar/resToggle.py" param2=1440')
    print('1080 | terminal=false bash="/usr/local/bin/python3" param1="/Users/ryancampbell/BitBar/resToggle.py" param2=1080')
elif sys.argv[1] == '1440':
    os.system(toggleRegularRes)
elif sys.argv[1] == '1080':
    os.system(toggleGameRes)
'''


