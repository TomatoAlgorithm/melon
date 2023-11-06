import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    ropes = []

    for _ in range(n):
        ropes.append(int(input()))

    ropes.sort()
    ropes.reverse()

    maxWeight = -1
    for i in range(len(ropes)):
        curWeight = (i+1) * ropes[i]
        if(maxWeight < curWeight):
            maxWeight = curWeight
    
    print(maxWeight)


solution()