# CP template Version 1.006
import os
import sys
# import heapq
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
from itertools import product
#import collections
from collections import deque
import copy
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
from heapq import heappush, heappop, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    global greqs, minTime
    greqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
    k = 3
    n = 5
    dfs([1 for _ in range(k)], n-k)
    return minTime

    # ######## INPUT AREA END ############
def dfs(sangdam, remain):# 모든 상담원 배치수
    global minTime
    if remain == 0:
        waitTime = dagi(sangdam)
        minTime = min(waitTime, minTime)
        return
    
    for i in range(len(sangdam)):
        newSangdam = list(sangdam)
        newSangdam[i] += 1
        dfs(newSangdam, remain - 1)

def dagi(sangdam):
    global greqs
    k = len(sangdam)
    que = [[0 for _ in range(sangdam[k]) ] for _ in range(k)]
    waitTime = 0
    
    for req in greqs:
        a = req[0]
        b = req[1]
        c = req[2] - 1
        

        endTime = heappop(que[c])
        if endTime <= a:
            heappush(que[c], a+b)
        elif len(que[c]) < sangdam[c]:
            heappush(que[c], endTime)
            heappush(que[c], a+b)
        else:
            waitTime += endTime - a
            heappush(que[c], endTime+b)

    return waitTime

global minTime, greqs
minTime = 100 * 300 + 1
greqs = []
# TEMPLATE ###############################

enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()