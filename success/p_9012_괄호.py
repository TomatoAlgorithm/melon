import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())

for i in range(n):
    stack = []
    statement = input()
    for state in statement:
        trigger = True
        if(state == '('):
            stack.append(state)
        elif(state == ')'):
            if(len(stack) == 0):
                trigger = False
                break
            stack.pop()
        if(len(stack)!=0):
            trigger=False
    if(trigger == True):
        print("YES")
    else:
        print("NO")
