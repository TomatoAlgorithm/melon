import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

s = input().split(' ')
n = int(s[0])
k = int(s[1])


live = deque()
tmp = deque()

for i in range(n):
    live.append(i+1)

res = '<'
idx = 0

for i in range(n):
    for j in range(k-1): 
        if(len(live) == 0) :
            live.append(tmp.popleft())
        tmp.append(live.popleft())
    if(len(live) == 0):
        res+=str(tmp.popleft())
    else:
        res+=str(live.popleft())
    for t in range(len(tmp)):
        live.append(tmp.popleft())

    if(i != n-1):
        res += ', '

res+='>'

print(res)