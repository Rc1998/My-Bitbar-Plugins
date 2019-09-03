#!/Users/ryancampbell/python/.venv/bitbar/bin/python

import os, sys

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

print('venv')
print('---')

for dir in listdir_fullpath('/Users/ryancampbell/python/.venv/'):
    environment_name = dir[33:]
    print('{0}/ | terminal=true bash=envon param1={0}'.format(environment_name))