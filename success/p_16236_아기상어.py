# CP template Version 1.006
import os
import sys
from collections import deque
# import heapq
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
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
    global n,maxPepole
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########
    n = int(input())

    board = []
    startPoint = []
    
    volume = 2
    growup = 2
    totalcnt = 0
    
    for i in range(n):
        row = list(map(int,input().split()))
        board.append(row)
        for j in range(n):
            if row[j] == 9:
                startPoint.append(i)
                startPoint.append(j)
                startPoint.append(0)
    
    board[startPoint[0]][startPoint[1]] = 0

    deq = deque()

    deq.append(startPoint)

    while(len(deq) != 0):
        curPoint = deq.popleft()

        movePoint = findFeed(volume,board,curPoint)

        if(movePoint[0] == -1 and movePoint[1] == -1):
            print(totalcnt)
            break
        else:
            totalcnt += movePoint[2]
            growup -= 1
            board[movePoint[0]][movePoint[1]] = 0
            deq.append(movePoint)
            if(growup == 0):
                volume += 1
                growup = volume


def findFeed(volume, board, curPoint):
    feedList = []
    selectedFeed = [-1,-1,401]

    for yIdx, row in enu(board,0) :
        for xIdx, feedVolume in enu(row, 0):
            if(feedVolume < volume and feedVolume != 0):
                feedList.append([yIdx, xIdx])
    
    for feedPoint in feedList:
        dist = getCount(board, curPoint, feedPoint, volume)
        if(dist[2] != -1):
            if(dist[2] < selectedFeed[2]):
                selectedFeed = dist
            elif dist[2] == selectedFeed[2]:
                if(dist[0] < selectedFeed[0]):
                    selectedFeed = dist
                elif(dist[0] == selectedFeed[0]):
                    if(dist[1] < selectedFeed[1]):
                        selectedFeed = dist

    return selectedFeed


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def getCount(board, curPoint, feedPoint, volume):
    boardQ = deque()
    boardQ.append([curPoint[0], curPoint[1], 0])
    visited = [[False for j in range(len(board))] for i in range(len(board))]
    
    while(len(boardQ) != 0):
        point = boardQ.popleft()

        if(point[0] == feedPoint[0] and point[1] == feedPoint[1]):
            return point

        for i in range(4):
            if isValid(board, volume, point, dx[i],dy[i]) and visited[point[0]+dy[i]][point[1]+dx[i]] == False:
                boardQ.append([point[0]+dy[i], point[1]+dx[i],point[2]+1])
                visited[point[0]+dy[i]][point[1]+dx[i]] = True
    
    return [-1,-1,-1]

def isValid(board, volume, point, dx, dy):
    y = point[0] + dy
    x = point[1] + dx

    if(x >= 0 and x<len(board) and y>=0 and y<len(board) and board[y][x] <= volume):
        return True
    
    return False
    

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