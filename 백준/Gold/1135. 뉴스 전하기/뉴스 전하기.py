N = int(input())
tree = list(map(int, input().split(' ')))
NodeDict = {}

def noticeNews(v):
    nodes = NodeDict[v]
    n = len(nodes)
    sizeCnt = []
    ret = 0
    for node in nodes:
        sizeCnt.append(noticeNews(node))
    
    sizeCnt.sort()
    for i in range(1, n+1):
        ret = max(ret, sizeCnt[i-1] + n-i) 
    
    return ret + 1

for i in range(0,N):
    NodeDict[i] = []

for i in range(1,N):
    NodeDict[tree[i]].append(i)

print(noticeNews(0)-1)