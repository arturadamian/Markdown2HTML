#!/usr/local/bin/python3
import sys
import os.path
from os import path

if len(sys.argv) < 2:
    sys.stdout.write("Usage: ./markdown2html.py README.md README.html\n")
    exit (1)
if not path.exists(sys.argv[1]):
    print("Missing ", sys.argv[1], file=sys.stderr)
    exit (1)
