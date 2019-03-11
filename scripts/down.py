#!/usr/bin/env python

import os
import sys

import constants

packageName = sys.argv[1]
print('''\033[93m
    | |                            
  __| | __ _ _ __   __ _  ___ _ __ 
 / _` |/ _` | '_ \ / _` |/ _ \ '__|
| (_| | (_| | | | | (_| |  __/ |   
 \__,_|\__,_|_| |_|\__, |\___|_|   
                    __/ |          
                   |___/           
''')
print(f'NOTE: This operation will remove the existing {packageName} \033[0m')
res = input('Do you wish to continue (y/n):')
if res != 'y':
  sys.exit(0)

print(f'Deleting {packageName}')
os.system(constants.DELETE_PACKAGE.format(packageName))
