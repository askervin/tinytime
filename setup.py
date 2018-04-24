#!/usr/bin/env python2

import glob
import time
import subprocess

from distutils.core import setup

try:
    git_hash = subprocess.check_output(["git", "describe", "--always"]).strip()
except:
    git_hash = "_"
try:
    timestamp = subprocess.check_output(["./tinytime", "epoch"]).strip()
except:
    timestamp = "zzzzzz"

setup(name         = 'tinytime',
      version      = '0.%s.g%s' % (timestamp, git_hash),
      description  = 'Tinytime presents epoch time with six symbols',
      author       = 'Antti Kervinen',
      author_email = 'antti.kervinen@gmail.com',
      packages     = [],
      py_modules   = ['tinytime'],
      scripts      = ['tinytime']
)
