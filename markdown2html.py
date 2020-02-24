#!/usr/bin/python3
"""
    script that takes an argument 2 strings:
        - First argument is the name of the Markdown file
        - Second argument is the output file name

"""

if __name__=='__main__':
    import sys
    from os import path
    
    mkd = {"#": "<h1>", "##": "<h2>", "###": "<h3>", "####": "<h4>", "#####": "<h5>", "######": "<h6>",}
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit (1)
    if not path.exists(sys.argv[1]) or not sys.argv[1].endswith('.md'):
        sys.stderr.write("Missing " + sys.argv[1] + "\n")
        exit (1)
    with open(sys.argv[1], mode="r") as x, open(sys.argv[2], mode="w") as y:
        for line in x:
            words = line.split(" ")
            if words[0] in mkd:
                htmlTag = mkd[words[0]]
            htmlFile = line.replace(words[0], "{}".format(htmlTag))
            htmlTag = htmlTag[:-1] + (" {}\n".format(htmlTag))
            y.write(htmlTag)

        exit(0)
