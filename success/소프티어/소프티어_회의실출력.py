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

    N, M = map(int, input().strip().split(' '))

    회의실 = {}
    출력용회의실 = []

    for _ in range(N):
      name = input()
      회의실[name] = [True for _ in range(9, 18)]
      출력용회의실.append(name)

    출력용회의실.sort()

    for _ in range(M):
      name, start, end = input().split(' ')
      start = int(start)
      end = int(end)

      for i in range(start, end):
        회의실[name][i-9] = False

    for 출력 in 출력용회의실:
      print('Room {0}:'.format(출력))
      if(회의실[출력].count(True) == 0):
        print('Not available')
      else:
        res = []
        cnt = 0
        cur = False
        for idx, b in enumerate(회의실[출력], 9):
          if(cur != b and b):
            cnt+=1
            cur = not cur
            res.append([idx])
          elif(cur != b and not b):
            res[-1].append[idx]
        print('{0} available:')
        for r in res:
          print('{0}-{1}'.format(r[0],r[1]))

    # ######## INPUT AREA END ############

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