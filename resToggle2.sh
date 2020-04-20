#!/bin/zsh

# Functions for each display option, includes the displayplacer command
function internal900() {
    /usr/local/bin/displayplacer "id:0AA6E386-CE2C-5EE2-CC95-F2B67DCDF861 res:1440x900 color_depth:4 scaling:on origin:(0,0)"
}

function internal1050() {
    /usr/local/bin/displayplacer "id:0AA6E386-CE2C-5EE2-CC95-F2B67DCDF861 res:1680x1050 color_depth:4 scaling:on origin:(0,0)"
}

function monitor1080 {
    /usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:1920x1080 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"
}

function monitor1440() {
    /usr/local/bin/displayplacer "id:C487FFEE-9620-8F3A-8BC2-A1A07CAF4201 res:2560x1440 hz:60 color_depth:8 scaling:on origin:(0,0) degree:0"
}

# parse the input parameter to detemine function to run
case "$1" in
    900)
    internal900
    ;;
    1050)
    internal1050
    ;;
    1080)
    monitor1080
    ;;
    1440)
    monitor1440
esac

# Menu items and bash commands for script rerun with a parameter
echo "resToggle | color='blue'"
echo "---"

echo "Internal Retina Display"
echo "900 | refresh=false terminal=false bash=$0 param1=900"
echo "1050 | refresh=false terminal=false bash=$0 param1=1050"
echo "---"

echo "Dell P2415Q"
echo "1080 | refresh=false terminal=false bash=$0 param1=1080"
echo "1440 | refresh=false terminal=false bash=$0 param1=1440"
echo "---"
