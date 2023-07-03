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
            cnt.append(1)
        elif(b == ')'):
            if(stick[-1] == bIdx-1):
                raser.append(stick.pop())
                cnt.pop()
                for i in range(len(cnt)):
                    cnt[i] += 1
            else:#stick[-1] ~ bIdx
                stick.pop()
                tot += cnt.pop()
    
    print(tot) 

solution()

