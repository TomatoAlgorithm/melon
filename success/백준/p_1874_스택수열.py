import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())

    printlist = []
    stack = [0]
    lastout = 0

    for i in range(n):
        lastNum = stack[-1]
        cur = int(input())
        if(cur < lastNum):
            print("NO")
            return

        for j in range(lastout+1, cur+1):
                printlist.append('+')
                stack.append(j)
        printlist.append('-')
        lastout = max(stack.pop(), lastout) 

    for pl in printlist:
        print(pl)
        
solution()