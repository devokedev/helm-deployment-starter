#!/usr/bin/env python

import argparse
import os
import sys

import constants

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', help='Package Name')
parser.add_argument('-c', '--chart', help='Chart Name')
args = parser.parse_args()

print(f'Installing package {args.name}')
os.system(constants.INSTALL_PACKAGE.format(**{
  'name': args.name, 
  'chart': args.chart
}))
