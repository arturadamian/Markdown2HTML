#!/usr/local/bin/python3
import sys
import os.path
from os import path

if len(sys.argv) < 3:
    sys.stdout.write("Usage: ./markdown2html.py README.md README.html\n")
    exit (1)
elif not path.exists(sys.argv[1]):
    sys.stdout.write("Missing " + sys.argv[1] + "\n")
    exit (1)
else:
    exit(0)
