import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    brackets = input()

    raser = []
    stick = []
    cnt = []
    tot = 0

    #생각해야 할 것 1. 쇠막대기인가 레이저인가
    for bIdx in range(len(brackets)):
        b = brackets[bIdx]
        if(b == '('):
            stick.append(bIdx)
            tot+=1
            cnt.append(1)
        elif(b == ')'):
            if(stick[-1] == bIdx-1):
                raser.append(stick.pop())
                cnt.pop()
                tot-=1
                tot+= len(cnt)
            else:#stick[-1] ~ bIdx
                stick.pop()
                cnt.pop()
    
    print(tot) 

solution()

