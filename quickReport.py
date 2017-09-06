"""
quickReport
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://ryanstutorials.net/programming-challenges/

Problem Statement:

Create a program which will accept a series of numbers (these could for
instance be a series of marks for an assessment) and then produce a quick
report. The report should include the mean, mode and median. You could also
include standard deviations if you're up to it. Your report should also
include a histogram of the values, eg:

	1 | ***
	2 | *
	3 | *******
	4 | ****
	5 | **

to represent [1,1,1,2,3,3,3,3,3,3,3,4,4,4,4,5,5]
"""

# from
# https://stackoverflow.com/questions/15389768/standard-deviation-of-a-list
def stdev(data):
    """Calculates the population standard deviation."""
    avg  = sum(data)/float(len(data))
    ss   = sum((x-avg)**2 for x in data)
    pvar = ss/len(data) # the population variance
    return pvar**0.5

def quickReport(l):
    """
    Executes the solution to the problem described in the problem statement
    """
    l.sort()
    hist = {}
    max_freq = 0
    i = 0
    while i < len(l):
        freq = 1
        while i < len(l) - 1 and l[i] == l[i + 1]:
            freq += 1
            i    += 1
        if freq > max_freq:
            max_freq = freq
            mode = l[i]
        print l[i], '|', '*' * freq
        i += 1

    if len(l) % 2 == 0:
        median = (l[len(l)/2] + l[len(l)/2 - 1]) / 2
    else:
        median = l[len(l)/2]

    print "Mean:", sum(l)/float(len(l))
    print "Median:", median
    print "Mode:", mode
    print "Standard deviation:", stdev(l)
