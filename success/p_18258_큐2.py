import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

queue = deque()
n = int(input())

for i in range(n):
    command = input().split(' ')
    
    if(command[0] == 'push'):
        queue.append(command[1])
        continue
    elif(command[0] == 'pop'):
        if(len(queue)>0):
            print(queue.popleft())
        else:
            print(-1)
        continue
    elif(command[0] == 'size'):
        print(len(queue))
        continue
    elif(command[0] == 'empty'):
        if(len(queue)>0):
            print(0)
        else:
            print(1)
        continue
    elif(command[0] == 'front'):
        if(len(queue)>0):
            print(queue[0])
        else:
            print(-1)
        continue
    elif(command[0] == 'back'):
        if(len(queue)>0):
            print(queue[-1])
        else:
            print(-1)
        continue        
    