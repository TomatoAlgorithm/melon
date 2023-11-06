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

        
    X = input().strip()
    Y = input().strip()
    Z = input().strip()
    k = int(input())

    Res = {}

    dfs(0, X, k, '', Res, 0)
    dfs(0, Y, k, '', Res, 0)
    dfs(0, Z, k, '', Res, 0)

    flag = False
    for key in sorted(Res.keys()):
        if Res[key] >= 2:
            print(key)
            flag = True
    if(not flag):
        print(-1)

    # ######## INPUT AREA END ############
def dfs(depth, string, k, cur, res, curIdx):
    if(depth == k):
        
        if res.get(cur):
            res[cur] = res.get(cur) + 1
        else:
            res[cur] = 1
        return
    
    for i in range(curIdx, len(string)):
        nCur = cur +string[i]
        dfs(depth+1, string, k, nCur, res, i+1)
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