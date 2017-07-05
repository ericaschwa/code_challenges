"""
GameOfInterval
By: Erica Schwartz (ericaschwa)
Solves problem as articulated here:
https://community.topcoder.com/stat?c=problem_statement&pm=14600&rd=16931

Problem Statement:

Fox Ciel is playing a single-player game called the 'Game of Interval'. 

In this problem an interval is a non-empty segment of consecutive integers. We
will use the notation [lo,hi] to denote an interval of all numbers x such that
lo <= x <= hi. For example, [1,1] is an interval containing the number 1, and
[3,5] is an interval containing the numbers 3, 4, and 5. In other words, [3,5]
is the set {3,4,5}. 

The union of intervals is simply the set union. Note that the union of two
intervals is not necessarily an interval. For example, the union of [1,1] and
[3,5] is the set {1,3,4,5} which is not an interval, but the union of [1,1],
[3,5], and [2,2] is an interval: the interval [1,5]. 

Initially, Fox Ciel has n cards: for each i from 0 to n-1, inclusive, there is
a card that contains the interval [i,i]. 

Ciel starts playing the game by choosing a non-negative integer k. 

Then, she can do the following operation k times:
1. Choose two different cards that contain intervals I1 and I2 such that their
   union is again an interval.
2. Create a new card with the interval that is the union of I1 and I2. (You
   also keep the two original cards.)

For example, if n = 4, Ciel can proceed as follows:
1. She chooses k = 2.
2. She chooses the cards with intervals [1,1] and [2,2] and produces a card
   with the interval [1,2].
3. She then chooses the cards with intervals [1,2] and [3,3] and produces a
   card with the interval [1,3].
4. Thus, she now has six cards: the original four with [0,0], [1,1], [2,2], and
   [3,3], and the two new ones with [1,2] and [1,3].
Once Ciel finishes merging the intervals, we will calculate the penalty p as
follows:

Suppose we ask Ciel to show us some cards such that the union of their
intervals is exactly the interval [L,R]. Let c(L,R) be the smallest number of
cards Ciel needs to show. The penalty p is the largest of all values c(L,R).
The maximum is taken over all pairs (L,R) such that 0 <= L <= R <= n-1. 

Intuitively, if Ciel chooses a very small k, the penalty p will be large. For
example, if she chooses k = 0, the penalty will be p = n because she'll need to
show n cards for the pair (L,R) = (0,n-1). On the other hand, if she prepares a
lot of cards, the penalty will be small. In particular, if she prepares all
possible cards, the penalty will be p = 1. 

Ciel's final score in this game is defined as s = k + p * n. Help Ciel play the
game in a way that will result in a reasonably small score. Note that you don't
have to find the best possible score: any solution with a score that does not
exceed 6415 will be accepted. 

Use a base-36 encoding when outputting your solution, as described below. We
will use digits and uppercase letters. The individual symbols have the
following values: '0' = 0, '9' = 9, 'A' = 10, 'Z' = 35. Any number between 0
and n-1 can now be expressed as a number in base-36 with exactly two digits.
For example, 4 is "04" and 84 is "2C" (as 84 = 2*36 + 12). An interval [L,R]
can be represented as the concatenation of L and R. For example, [0,83] will be
"002B". 

Output a String of length 4*k: the concatenation of the k intervals you want to
produce, in the order in which you'll produce them. For example, if k = 3 and
these intervals are [1,2], [2,3], [1,3], then you should output "010202030103".
The value of k must not exceed 4500. (I.e., the length of your output must not
exceed 4500*4 = 18000). We guarantee the solution always exist under these
constraints.
"""

from math import factorial

def to_base36(n):
    """
    Given int n, returns string containing its 2-digit, base-36 representation
    """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result_reverse = ''
    while n > 0:
        digit = n % 36
        if digit < 10:
            result_reverse += str(digit)
        else:
            result_reverse += letters[digit-10]
        n /= 36
        if n == 0 and len(result_reverse) < 2:
            result_reverse += '0'
    result = ''
    for i in xrange(len(result_reverse) - 1, -1, -1):
        result += result_reverse[i]
    return result

def output_intervals(l):
    """
    Given a list l of intervals, output them in the format as specified by the
    problem statement
    """
    result = ''
    for interval in l:
        result += to_base36(interval[0]) + to_base36(interval[1] - 1)
    return result

def score(k, p, n):
    """
    Given the values for k, p, and n, returns the score for that round
    """
    return k + p * n

def intervals_overlap(a, b):
    """
    Returns True if intervals a and b overlap, False otherwise
    """
    return a[0] <= b[1] and b[0] <= a[1]

def merge_intervals(a, b):
    """
    Returns result of merging intervals a and b
    """
    if a[0] < b[0]:
        return (a[0], b[1])
    return (b[0], a[1])

def take_turns(intervals, k):
    """
    Takes k turns in the game
    """
    if k == 0: return [intervals]
    intervals_set = []
    for i in xrange(len(intervals)):
        for j in xrange(i+1, len(intervals)):
            if intervals_overlap(intervals[i], intervals[j]):
                new_interval   = merge_intervals(intervals[i], intervals[j])
                intervals.append(new_interval)
                intervals_set += take_turns(intervals, k - 1)
    return intervals_set

def generate_intervals(n, k):
    """
    Returns a list of all interval sets that can be generated from n cards in k
    turns
    """
    intervals    = [(i, i + 1) for i in xrange(n)]
    interval_set = take_turns(intervals, k)
    return interval_set

def compare(interval1, interval2):
    """
    Compares 2 intervals, returns whether the first interval is considered to be
    'before' the second (based on their end points).
    """
    return (interval1[1] < interval2[1])

def calculate_penalty(intervals, l, r):
    """
    Given intervals and [L, R], returns the number of intervals in the list
    needed to form the [L, R] interval
    """
    # https://cs.stackexchange.com/questions/9531/
    # finding-the-minimum-subset-of-intervals-covering-the-whole-set
    r += 1
    curr_range = r - l
    intervals  = sorted(intervals, cmp=compare)
    T = [[float('inf') for k in xrange(len(intervals))] for j in xrange(curr_range)]
    for k in xrange(len(intervals)): T[0][k] = 0

    for j in xrange(curr_range):
        for k in xrange(1, len(intervals)):
            if intervals[k][1] - l >= j and intervals[k][0] - l < len(T) and intervals[k][0] - l > -1:
                T[j][k] = min(T[j][k-1], min(T[intervals[k][0] - l]) + 1)

    return min(T[curr_range - 1])

def play_round(n, k):
    """
    Given values for n and k, plays a round of the game and returns the minimum
    penalty and the intervals that produced it
    """
    intervals_set = generate_intervals(n, k)
    for intervals in intervals_set:
        p = 0
        for l in xrange(n):
            for r in xrange(l, n):
                cost = calculate_penalty(intervals, l, r)
                if cost > p: p = cost
        s = score(k, p, n)
        if s <= 6415: return (intervals, s)

def construct(n):
    """
    Executes the solution to the problem described in the problem statement
    """
    min_s         = float('inf')
    min_interval  = None
    num_intervals = factorial(n)/factorial(n-2)/2

    for k in xrange(num_intervals + 1):
        round_result = play_round(n, k)
        if round_result is not None:
        	intervals, s = round_result
        	if s < min_s:
        		min_s        = s
        		min_interval = intervals

    return output_intervals(min_interval)
