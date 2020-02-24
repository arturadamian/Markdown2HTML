#!/usr/bin/python3
"""
    script that takes an argument 2 strings:
        - First argument is the name of the Markdown file
        - Second argument is the output file name

"""

if __name__=='__main__':
    import sys
    from os import path

    if len(sys.argv) < 3:
        sys.stdout.write("Usage: ./markdown2html.py README.md README.html\n")
        exit (1)
    if not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
        sys.stdout.write("Missing " + sys.argv[1] + "\n")
        exit (1)
    with open(sys.argv[1], mode="r") as f:
        exit(0)
