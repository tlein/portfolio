#!/usr/bin/env python3

from __future__ import print_function

import subprocess
import signal
import sys

JEKYLL_PROCESS = subprocess.Popen(["bundle", "exec", "jekyll", "serve"])
PUG_LAYOUT_PROCESS = subprocess.Popen("pug -w -o _layouts/ _layouts/pug/*.pug", shell=True)
PUG_PAGE_PROCESS = subprocess.Popen("pug -w -o . ./*.pug", shell=True)

def crash_handler(signal, frame):
    """Handles Ctrl+C crash to kill the jekyll process"""
    print("\nGoodbye")
    JEKYLL_PROCESS.kill()
    PUG_LAYOUT_PROCESS.kill()
    PUG_PAGE_PROCESS.kill()
    sys.exit(0)

signal.signal(signal.SIGINT, crash_handler)
signal.pause()
