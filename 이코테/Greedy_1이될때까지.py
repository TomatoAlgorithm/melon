import sys

def input():
    return sys.stdin.readline().rstrip()

def mySolution(n, k):
    cnt = 0
    while(n != 1):
        if(n % k == 0):
            n /= k
        else:
            n -=1
        cnt+=1
    print(cnt)


n, k = map(int, input().split(' '))
mySolution(n,k)