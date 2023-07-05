import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()

def solution():
    tot = int(input())

    for i in range(tot):
        n,m = input().split(' ')
        printlist = input().split(' ')
        printlist = list(map(int, printlist))

        cnt = 0
        idx = int(m)
        printor = deque(printlist)

        while(len(printor)>0):
            cur = int(printor.popleft())
            if(len(printor)>0 and cur < max(printor)):
                printor.append(cur)
            else:
                cnt += 1
                if(idx == 0):
                    print(cnt)
                    break
            idx -= 1
            if(idx < 0):
                idx=len(printor)-1

solution()