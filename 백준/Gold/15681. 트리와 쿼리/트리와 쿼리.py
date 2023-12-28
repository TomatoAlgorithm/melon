import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, R, Q = map(int, input().split(' '))

NodeDict = {}
parents = [0] * (N+1)
counts = [0] * (N+1)

def setParent(v, p):
    count = 1
    for node in NodeDict[v]:
        if(node != p):
            count += setParent(node, v)
    
    counts[v] = count
    return count

for i in range(1,N+1):
    NodeDict[i] = []

for _ in range(N-1):
    U, V = map(int, input().split(' '))
    NodeDict[U].append(V)
    NodeDict[V].append(U)

NodeDict[R].append(-1)

setParent(R, -1)

for _ in range(Q):
    print(counts[int(input())])