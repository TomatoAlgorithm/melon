import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    tops = input().split(' ')

    receive = deque()

    for h in range(len(tops)-1,-1,-1):
        height = tops[h]
        trigger = False
        for bh in range(h-1,-1,-1):
            if(tops[bh]>=height):
                receive.appendleft(bh+1)
                trigger = True
                break
        if(trigger == False):
            receive.appendleft(0)
    
    print([*receive],sep=' ')

solution()

