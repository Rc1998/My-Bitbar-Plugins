#!/Users/ryancampbell/python/.venv/bitbar/bin/python3

from os import system
import sys
from AppKit import NSScreen

monitor1440 = '/usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:2560x1440 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"'
monitor1080 = '/usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:1920x1080 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"'

builtIn1050 = '/usr/local/bin/displayplacer "id:0AA6E386-CE2C-5EE2-CC95-F2B67DCDF861 res:1680x1050 color_depth:4 scaling:on origin:(0,0) degree:0"'
builtIn900 = '/usr/local/bin/displayplacer "id:0AA6E386-CE2C-5EE2-CC95-F2B67DCDF861 res:1440x900 color_depth:4 scaling:on origin:(0,0) degree:0"'