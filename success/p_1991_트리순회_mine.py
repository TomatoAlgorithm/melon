# CP template Version 1.006
import os
import sys
# import heapq
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
import copy
from itertools import product
#import collections
from collections import deque
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
    n = int(input())

    tree = [[] for i in range(91)]

    for i in range(n):
        element = list(map(str, input().rstrip().split(' ')))
        tree[ord(element[0])].append(ord(element[0]))
        tree[ord(element[0])].append(ord(element[1]))
        tree[ord(element[0])].append(ord(element[2]))
    
    prefix(tree)
    infix(tree)
    postfix(tree)


def prefix(tree):
    deq = deque()

    deq.append(65)

    res =''

    while(len(deq) != 0):
        cur = deq.popleft()

        res+=chr(cur)

        left = tree[cur][1]
        right = tree[cur][2]

        if(right != ord('.')):
            deq.appendleft(right)
        if(left != ord('.')):
            deq.appendleft(left)

    print(res)
    return 0

def infix(tree):
    cp_tree = copy.deepcopy(tree)
    deq = deque()

    deq.append(65)

    res=''

    while(len(deq) != 0):
        cur = deq.popleft()

        left = cp_tree[cur][1]
        right = cp_tree[cur][2]

        cp_tree[cur][1] = ord('.')
        cp_tree[cur][2] = ord('.')

        if(left == ord('.') and right == ord('.')):
            res+=chr(cur)
            continue

        if(right != ord('.')):
            deq.appendleft(right)
        deq.appendleft(cur)
        if(left != ord('.')):
            deq.appendleft(left)
    
    print(res)
    return 0

def postfix(tree):
    cp_tree = copy.deepcopy(tree)
    deq = deque()

    deq.append(65)

    res=''

    while(len(deq) != 0):
        cur = deq.popleft()

        left = cp_tree[cur][1]
        right = cp_tree[cur][2]

        cp_tree[cur][1] = ord('.')
        cp_tree[cur][2] = ord('.')

        if(left == ord('.') and right == ord('.')):
            res+=chr(cur)
            continue

        deq.appendleft(cur)
        if(right != ord('.')):
            deq.appendleft(right)
        if(left != ord('.')):
            deq.appendleft(left)
        
    print(res)
    return 0


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