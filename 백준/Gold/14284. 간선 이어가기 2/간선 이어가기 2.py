import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 5000 * 5000

n, m = map(int, input().split(' '))
graph = {}

for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):
    a, b, c = map(int, input().split(' '))

    graph[a][b] = c
    graph[b][a] = c

s, t = map(int, input().split(' '))

que = []
dist = [INF] * (n+1)
dist[s] = 0
heappush(que, (0, s))

while que:
    cur_dist, cur_node = heappop(que)

    if cur_dist > dist[cur_node]:
        continue

    for next_node, next_weight in graph[cur_node].items():
        distance = next_weight + cur_dist
        if distance < dist[next_node]:
            dist[next_node] = distance
            heappush(que, (distance, next_node))

print(dist[t])