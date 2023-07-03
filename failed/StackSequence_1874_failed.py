import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())

    printlist = []
    outNum = []
    stack = [0]

    for i in range(n):
        lastNum = stack[-1]
        cur = int(input())
        if(cur < lastNum):
            print("NO")
            return

        for j in range(lastNum+1, cur+1):
            if(j not in outNum):#시간초과 코드
                printlist.append('+')
                stack.append(j)
        printlist.append('-')
        outNum.append(stack.pop())

    for pl in printlist:
        print(pl)
        
