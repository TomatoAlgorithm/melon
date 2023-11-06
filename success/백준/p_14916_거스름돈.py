import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    trigger = False
    for i in range(n//5,-1,-1):
        tmp = n-i*5

        if(tmp % 2 == 0):
            trigger = True
            print(i+tmp//2)
            break
    if trigger == False:
        print(-1)

solution()