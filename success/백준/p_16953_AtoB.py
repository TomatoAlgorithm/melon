import sys

def input():
    return sys.stdin.readline().rstrip()
A = -1
B = -1
minCnt = sys.maxsize
trigger = False
def solution():
    global A,B,minCnt,trigger
    A, B = map(int,input().split(' '))

    dfs(0,A,0,0)

    print(minCnt if trigger else -1)

def dfs(depth, n, cnt2, cnt3):
    global A,B,minCnt,trigger
    if(n == B):
        trigger = True
        minCnt = min(depth+1,minCnt)
        return
    elif(n>B):
        return
    
    for i in range(2):
        tmp = n
        if(i==0):
            tmp = int(str(n)+'1')
            dfs(depth+1,tmp,cnt2+1,cnt3)
        else:
            tmp *= 2
            dfs(depth+1,tmp,cnt2,cnt3+1)

solution()