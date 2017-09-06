"""
correctHTML
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://ryanstutorials.net/programming-challenges/

Problem Statement:

Create a program which will read in a file containing HTML and identify
lines with incorrectly nested tags. This is an example of correctly nested
tags:

<H1>This is my <span>heading</span></H1>

And this is an example of incorrectly nested tags:

<H1>This is my <span>heading</H1></span>
"""

import re

def check_tags(l):
    """
    Given line of HTML, checks that HTML tags match. If not, prints the line.
    """
    # start on outside working inwords, checking first and last tags match
    stack = []
    for item in l:
        if   item[-2] == '/' or item[1] == '!':
           continue # deal with self-closing tags and comments
        elif item[ 1] == '/':
           root  = item[2 : -1].split()[0]
           try:
                match = stack.pop()
           except: return False # closing tag without an opener
           if root != match:
               return False
        else:
           root = item[1 : -1].split()[0]
           stack.append(root) 
    return True

def correct(filename):
    """
    Executes the solution to the problem described in the problem statement
    """
    with open(filename) as f:
        html  = f.read()
        lines = html.split('\n')

    for line in lines:
        l = re.findall(r'<[^>]+>', line)
        if len(l) == 1: continue # deal with lines containing only 1 tag
        correct = check_tags(l)
        if not correct:
            print "Incorrect:", line

