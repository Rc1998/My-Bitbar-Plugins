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

ICON="iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEvGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS41LjAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgZXhpZjpQaXhlbFhEaW1lbnNpb249IjMyIgogICBleGlmOlBpeGVsWURpbWVuc2lvbj0iMzIiCiAgIGV4aWY6Q29sb3JTcGFjZT0iMSIKICAgdGlmZjpJbWFnZVdpZHRoPSIzMiIKICAgdGlmZjpJbWFnZUxlbmd0aD0iMzIiCiAgIHRpZmY6UmVzb2x1dGlvblVuaXQ9IjIiCiAgIHRpZmY6WFJlc29sdXRpb249IjE0NC4wIgogICB0aWZmOllSZXNvbHV0aW9uPSIxNDQuMCIKICAgcGhvdG9zaG9wOkNvbG9yTW9kZT0iMyIKICAgcGhvdG9zaG9wOklDQ1Byb2ZpbGU9InNSR0IgSUVDNjE5NjYtMi4xIgogICB4bXA6TW9kaWZ5RGF0ZT0iMjAyMC0wNC0yMFQxNDoxOTo0NC0wNTowMCIKICAgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMC0wNC0yMFQxNDoxOTo0NC0wNTowMCI+CiAgIDx4bXBNTTpIaXN0b3J5PgogICAgPHJkZjpTZXE+CiAgICAgPHJkZjpsaQogICAgICBzdEV2dDphY3Rpb249InByb2R1Y2VkIgogICAgICBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZmZpbml0eSBEZXNpZ25lciAoTWFyIDMxIDIwMjApIgogICAgICBzdEV2dDp3aGVuPSIyMDIwLTA0LTIwVDE0OjE5OjQ0LTA1OjAwIi8+CiAgICA8L3JkZjpTZXE+CiAgIDwveG1wTU06SGlzdG9yeT4KICA8L3JkZjpEZXNjcmlwdGlvbj4KIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+Cjw/eHBhY2tldCBlbmQ9InIiPz6mpM5uAAABgmlDQ1BzUkdCIElFQzYxOTY2LTIuMQAAKJF1kc8rRFEUxz/zQ8SImIWFxaQZKyNGTWyUmYSSpjHKYDPzzA81P17vzaTJVtlOUWLj14K/gK2yVopIycrCmtig5zyjZpI5t3PP537vPad7zwVrJKNkdfsAZHMFLTwRcM1HF1yNT9hx0oGH3piiq2Oh0DR17f0WixmvvWat+uf+tZblhK6ApUl4VFG1gvCk8PRqQTV5S9ippGPLwifCfZpcUPjG1OMVfjY5VeFPk7VIOAjWdmFXqobjNayktaywvBx3NlNUfu9jvsSRyM3NSuwR70YnzAQBXEwxThA/g4zI7MeLj35ZUSd/4Cd/hrzkKjKrlNBYIUWaAn2iFqV6QmJS9ISMDCWz/3/7qieHfJXqjgA0PBrGqwcaN+GrbBgfB4bxdQi2BzjPVfPz+zD8Jnq5qrn3oG0dTi+qWnwbzjag616NabEfySZuTSbh5Rhao9B5Bc2LlZ797nN0B5E1+apL2NmFXjnftvQNdL9n7JK77jgAAAAJcEhZcwAAFiUAABYlAUlSJPAAAACqSURBVFiF7ZRBCoMwEACXSt8i+aDfMa/zEV6mh0aJYslGuhuEzHlhhmQTkU7n6QADEFHQPMIsQBthGpAiArC2OoERWFrtQFFuFlCQH67DW77w3YloEqCQj2lufx3u8mx+AGITeR5RI7kcviuvBpjPEW7yJCOPcJVnAVtEcJWfAuD3324jvwjwlSsCbOWFgBUI/3S9KuffIjJR86ncQbEDs2mEIsA+otPx4gMCoT7nFC4FPAAAAABJRU5ErkJggg=="

# Menu items and bash commands for script rerun with a parameter
echo " | image=$ICON color=white"
echo "---"

echo "Internal Retina Display"
echo "900 | refresh=false terminal=false bash=$0 param1=900"
echo "1050 | refresh=false terminal=false bash=$0 param1=1050"
echo "---"

echo "Dell P2415Q"
echo "1080 | refresh=false terminal=false bash=$0 param1=1080"
echo "1440 | refresh=false terminal=false bash=$0 param1=1440"
echo "---"
