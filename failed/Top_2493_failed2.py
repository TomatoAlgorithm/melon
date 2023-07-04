import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

#시간초과
def solution():
    n = int(input())
    tops = input().split(' ')
    tops = list(map(int, tops))
    receive = []
    
    maxheight = 0
    maxidx = 0

    for tIdx, topHeight in enumerate(tops, 0) :
        if(topHeight > maxheight):
            maxheight = topHeight
            maxidx = tIdx
        
        trig = False
        for i in range(tIdx-1,maxidx-1,-1):
            if(tops[i] >= topHeight):
                receive.append(i+1)
                trig = True
                break
        
        if(trig == False):
            receive.append(0)
    
    print([*receive],sep=' ')

solution()

