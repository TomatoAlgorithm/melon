N = int(input())

weights = list(map(int, input().split(' ')))
global res
res = 0

def dfs(weights, cur):
    global res
    if len(weights) == 2:
        res = max(res, cur)
        return
    
    for i in range(1, len(weights)-1):
        new_weights = weights[:]
        del new_weights[i]
        dfs(new_weights, cur+(weights[i-1] * weights[i+1]))
dfs(weights, 0)
print(res)