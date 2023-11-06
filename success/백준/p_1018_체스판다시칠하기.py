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


    # 예시 배열
    arr = deque([1, 3, 5, 2, 1, 3, 1])

    # 함수 호출 및 결과 출력
    result = findMaximumGreatness(arr)
    print(result)  # 최대 "위대함" 값 출력

def findMaximumGreatness(arr):
    n = len(arr)
    sorted_arr = sorted(arr)
    
    sorted_arr.pop()

    # 각 요소보다 큰 요소의 개수를 저장하는 리스트
    greater_count = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if sorted_arr[j] > sorted_arr[i]:
                greater_count[i] += 1

    max_greatness = 0

    for i in range(n):
        if greater_count[i] > max_greatness:
            max_greatness = greater_count[i]

    return max_greatness
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