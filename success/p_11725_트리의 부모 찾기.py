import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    parentList = [0] * (n+1)
    treeList = [[] for i in range(n+1)] 

    for i in range(n-1):
        element = list(map(int,input().split(' ')))
        treeList[element[0]].append(element[1])
        treeList[element[1]].append(element[0])
    
    deq = deque()

    parentList[1] = -1

    for i in treeList[1]:
        deq.append(i)
        parentList[i] = 1
    
    while len(deq) != 0:
        cur = deq.popleft()

        for i in treeList[cur]:
            if(parentList[i] == 0):
                deq.append(i)
                parentList[i] = cur
    
    for j in range(2,n+1):
        print(parentList[j])

    
solution()