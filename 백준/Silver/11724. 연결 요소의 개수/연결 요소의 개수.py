def getParent(arr, a):
    if arr[a] == a:
        return a
    
    parent = getParent(arr, arr[a])
    arr[a] = parent
    return parent

def union(arr, a, b):
    a = getParent(arr, a)
    b = getParent(arr, b)
    
    if a > b:
        arr[a] = b
    else:
        arr[b] = a
        
N, M = map(int, input().split(' '))
arr = [i for i in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split(' '))
    
    union(arr, u, v)
    
for i in range(N+1):
    getParent(arr, i)
    
res = set(arr)
print(len(res)-1)