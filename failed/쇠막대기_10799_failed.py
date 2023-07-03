import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    brackets = input()

    raser = []
    stick = []
    cnt = 0

    tmp = 0
    lastidx = 0

    #생각해야 할 것 1. 쇠막대기인가 레이저인가
    for bIdx in range(len(brackets)):
        b = brackets[bIdx]
        if(b == '('):
            stick.append(bIdx)
        elif(b == ')'):
            if(stick[-1] == bIdx-1):
                raser.append(stick.pop())
            else:
                for i in range(len(stick)-1,-1,-1):
                    if (isinstance(stick[i],int)):
                         stick[i] = (stick[i],bIdx)
                         break
    
    for ss in stick:
        cnt += brackets[ss[0]:ss[1]].count('()')+1
    print(cnt) 

solution()

