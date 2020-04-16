#!/Users/ryancampbell/python/.venv/bitbar/bin/python3

# <bitbar.title>resToggle 2</bitbar.title>
# <bitbar.version>v2.0</bitbar.version>
# <bitbar.author>Ryan Campbell</bitbar.author>
# <bitbar.author.github>Rc1998</bitbar.author.github>
# <bitbar.desc>Lists resolutions for screens and allows toggling between them.</bitbar.desc>
# <bitbar.dependencies>python, displayplacer, AppKit</bitbar.dependencies>

from os import system
import sys
from AppKit import NSScreen

# Display placer commands for each display and resolution
monitor1440 = '/usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:2560x1440 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"'
monitor1080 = '/usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:1920x1080 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"'

builtIn1050 = '/usr/local/bin/displayplacer "id:0AA6E386-CE2C-5EE2-CC95-F2B67DCDF861 res:1680x1050 color_depth:4 scaling:on origin:(0,0) degree:0"'
builtIn900 = '/usr/local/bin/displayplacer "id:0AA6E386-CE2C-5EE2-CC95-F2B67DCDF861 res:1440x900 color_depth:4 scaling:on origin:(0,0) degree:0"'

# Construct the menu
print('●')
print("---")

print("Internal Retina Display")
print('900 | refresh=false terminal=false bash="/Users/ryancampbell/python/.venv/bitbar/bin/python" param1="/Users/ryancampbell/BitBar/resToggle2.py" param2=900')
print('1050 | refresh=false terminal=false bash="/Users/ryancampbell/python/.venv/bitbar/bin/python" param1="/Users/ryancampbell/BitBar/resToggle2.py" param2=1050')
print("---")

print("Dell P2415Q")
print('1080 | refresh=false terminal=false bash="/Users/ryancampbell/python/.venv/bitbar/bin/python" param1="/Users/ryancampbell/BitBar/resToggle2.py" param2=1080')
print('1440 | refresh=false terminal=false bash="/Users/ryancampbell/python/.venv/bitbar/bin/python" param1="/Users/ryancampbell/BitBar/resToggle2.py" param2=1440')
print("---")

def toggle(input):
    if  input == '900':
        system(builtIn900)
    elif input == '1050':
        system(builtIn1050)
    elif input == '1080':
        system(monitor1080)
    elif input == '1440':
        system(monitor1440)


if len(sys.argv) > 1:
    toggle(sys.argv[1])