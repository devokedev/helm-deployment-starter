#!/usr/bin/env python

import argparse
import getpass
import os
import sys

import constants

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--namespace", help="Namespace")
args = parser.parse_args()

def init():
  
  print(f'Creating Namespace: {args.namespace}')
  os.system(constants.CREATE_NAMESPACE.format(args.namespace))

  print(f'Setting default namespace to {args.namespace}')
  os.system(constants.SET_DEFAULT_NAMESPACE.format(args.namespace))
  
  print('Creating Gitlab Image Pull Secret')
  os.system(constants.REGISTRY_SECRET.format(**{
    'secret_name': constants.IMAGE_PULL_SECRET,
    'docker-server': input(f'Please enter docker-server (defaults to \
      {constants.DEFAULT_REGISTRY_SERVER}): ') or constants.DEFAULT_REGISTRY_SERVER,
    'docker-username': input('Please enter your username: '),
    'docker-password': getpass.getpass('Please enter your password: '),
    'docker-email': input('Please enter your email: ')
  }))

init()
