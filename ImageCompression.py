"""
ImageCompression
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14612&rd=16884

Problem Statement:

You have a rectangular bitmap that consists of n rows by m columns of pixels.
You are given the bitmap encoded as a String[] image. Each pixel of the bitmap
is either black or white. Black pixels are represented by the character '0',
white ones by '1'.

You are also given an int k that divides both n and m. You want to check
whether you can compress the bitmap by shrinking it k times in each dimension.
More precisely, the compression works as follows:

Divide the bitmap into blocks of size k times k pixels. Check whether each
block consists of pixels of a single color only. If some block contains both
black and white pixels, the bitmap cannot be compressed. Compress the bitmap by
shrinking each block into a single pixel of the respective color. Determine
whether we can compress the given bitmap for the given k. If we can, return
"Possible", otherwise, return "Impossible". Note that the return value is case-
sensitive.
"""

def is_possible(strs, k):
    """
    Executes the solution to the problem described in the problem statement
    """
    for i in xrange(len(strs) / k):
        rows          = strs[i * k: (i + 1) * k]
        for j in xrange(len(strs[0]) / k):
            piece     = [row[j * k: (j + 1) * k] for row in rows]
            target    = piece[0]
            for s in piece:
                if s != target:
                    return "Impossible"
    return "Possible"
