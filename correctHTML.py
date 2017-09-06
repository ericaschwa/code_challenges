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

def correct(filename):
    """
    Executes the solution to the problem described in the problem statement
    """
    with open(filename) as f:
         html = f.read()
    l = re.findall(r'</\w+>|<\w+>', html)
    for i in xrange(len(l)/2):
        if l[len(l) - i - 1] != l[i][0] + '/' + l[i][1:]:
            return False
    return True
