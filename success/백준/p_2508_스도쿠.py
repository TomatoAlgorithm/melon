# CP template Version 1.006
import os
import sys
from collections import deque
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
#from heapq import heappush, heappop, heapreplace
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False

sudoku = []
zeropoint = []    

def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    for i in range(9):
        sudoku.append(list(map(int,input().split(' '))))
        for idx, s in enumerate(sudoku[i], 0):
            if(s == 0):
                zeropoint.append((i,idx))
    
    dfs(0)

    # ######## INPUT AREA END ############

def dfs(depth):
    if depth == len(zeropoint):
        for s in sudoku:
            print(*s,sep=' ')
        exit(0)
    
    for i in range(1,10):
        x=zeropoint[depth][0]
        y=zeropoint[depth][1]

        if(promising(x,y,i)==True):
            sudoku[x][y]=i
            dfs(depth+1)
            sudoku[x][y]=0

def promising(x,y,n):
    # # 미리만들기
    # # 시간 초과
    # rows = sudoku[x]
    # if rows.count(n) != 0:
    #     return False
    
    # for문으로 확인
    # 최선일 경우 더 빠름
    for r in sudoku[x]:
        if(r==n):
            return False
        
    for k in range(9):
        if(sudoku[k][y] == n):
            return False

    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if sudoku[nx+i][ny+j] == n:
                return False

    return True

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
    
    return True