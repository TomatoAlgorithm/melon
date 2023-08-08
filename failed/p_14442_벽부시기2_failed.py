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

maze = []
visited=[]
N = -1
M = -1
K = -1
def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    global N,M,K

    N, M, K = map(int,input().split(' '))
    K+=1
    for i in range(N):
        line = list(map(int, input().rstrip()))
        vLine = [[False for j in range(K)] for i in range(M)]
        maze.append(line)
        visited.append(vLine)
    
    for i in range(K):
        visited[0][0][i] = True
    # visited1 = copy.deepcopy(visited)

    deq = deque()
    deq.append([0,0,1,0])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while len(deq) != 0:
        cur = deq.popleft()

        if(cur[0] == N-1 and cur[1] == M-1):
            print(cur[2])
            break

        for i in range(4):
            res = isValid(cur[0],cur[1],dy[i],dx[i],cur[3])
            if res[0]:
                deq.append([cur[0] + dy[i], cur[1]+dx[i],cur[2]+1, res[1]])
                for j in range(K):        
                    if res[1] == j:
                        for a in range(j,K):
                            visited[cur[0]+dy[i]][cur[1]+dx[i]][a] = True
                        break
    else:
        print(-1)

def isValid(cury, curx, dy, dx, breakcnt):
    y = cury+dy
    x = curx+dx
    
    if(y >=0 and y < N and x >= 0 and x < M):
        if(maze[y][x] == 0 and not visited[y][x][breakcnt]):
            return [True, breakcnt]
        elif(maze[y][x] == 1  and not visited[y][x][breakcnt]):
            if(breakcnt < K-1):
                breakcnt += 1
                return [True, breakcnt]

    return [False, -1]

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