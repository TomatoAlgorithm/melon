import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())

    ballonlist = input().split(' ')
    idx = []
    
    for i in range (1,N+1):
        idx.append(i)

    idxq = deque(idx)
    ballonq = deque(ballonlist)
    res = ''

    while(len(ballonq) > 0):
        curidx = idxq.popleft()
        dist = int(ballonq.popleft())
        res += str(curidx)+' '

        if(len(idxq) == 0):
            break

        if(dist>0):
            for i in range(1,dist):
                ballonq.append(ballonq.popleft())
                idxq.append(idxq.popleft())
        else:
            for i in range(abs(dist)):
                ballonq.appendleft(ballonq.pop())
                idxq.appendleft(idxq.pop())


    print(res[:-1])

    


solution()

