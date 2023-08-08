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
dist=[]
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
        vLine = [[0 for j in range(K)] for i in range(M)]
        maze.append(line)
        dist.append(vLine)
    
    for i in range(K):
        dist[0][0][i] = 1
    # visited1 = copy.deepcopy(dist)

    deq = deque()
    deq.append([0,0,0,True])

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    while len(deq) != 0:
        y,x,z,b = deq.popleft()

        if(y == N-1 and x == M-1):
            print(dist[y][x][z])
            break

        trig = False

        for i in range(4):
            wy = y+dy[i]
            wx = x+dx[i]
            if (wx >= 0 and wx < M and wy>=0 and wy < N):
                if(maze[wy][wx] == 0):
                    if(dist[wy][wx][z] == 0):
                        dist[wy][wx][z] = dist[y][x][z] + 1
                        deq.append([wy,wx,z,not b])
                elif(maze[wy][wx] == 1 and z < K-1):
                    if(dist[wy][wx][z+1] == 0):
                        if b:# 여기서 추가 변수로 밤낮을 체크하니까 시간초과가 난다
                            dist[wy][wx][z+1] = dist[y][x][z] + 1
                            deq.append([wy,wx,z+1,not b])
                        else:
                            trig=True
                            deq.append([y,x,z,not b])
        if trig:
            dist[y][x][z] += 1

    else:
        print(-1)

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