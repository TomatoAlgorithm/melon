import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
    
l.sort(key=lambda x : (x[0],x[1]))