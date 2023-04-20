# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 13:03:48 2022

@author: 15075
"""
import os

import sys
from glob import glob

from distutils.sysconfig import get_python_inc

configcommand = os.environ.get('SDL_CONFIG', 'sdl-config',)
configcommand = configcommand + ' --version --cflags --libs'
localbase = os.environ.get('LOCALBASE', '')
