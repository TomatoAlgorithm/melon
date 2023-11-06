import sys

def input():
    return sys.stdin.readline().rstrip()

stack = []
n = int(input())

for i in range(n):
    command = input().split(' ')
    
    if(command[0] == 'push'):
        stack.append(command[1])
        continue
    elif(command[0] == 'pop'):
        if(len(stack)>0):
            print(stack.pop(-1))
        else:
            print(-1)
        continue
    elif(command[0] == 'size'):
        print(len(stack))
        continue
    elif(command[0] == 'empty'):
        if(len(stack)>0):
            print(0)
        else:
            print(1)
        continue
    elif(command[0] == 'top'):
        if(len(stack)>0):
            print(stack[-1])
        else:
            print(-1)
        continue
    