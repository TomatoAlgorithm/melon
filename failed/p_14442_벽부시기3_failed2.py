import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

maze = []
dist=[]

N, M, K = map(int,input().split(' '))
K+=1
# 4차원으로 변경해서 진행해 보았으나 여전히 시간초과가 일어남
for i in range(N):
    line = list(map(int, input().rstrip()))
    vLine = [[[0 for _ in range(2)] for _ in range(K)] for _ in range(M)]
    maze.append(line)
    dist.append(vLine)

for i in range(K):
    for j in range(2):
        dist[0][0][i][j] = 1

deq = deque()
deq.append([0,0,0,0])

dx = [1,0,-1,0]
dy = [0,1,0,-1]

while len(deq) != 0:
    y,x,z,b = deq.popleft()

    if(y == N-1 and x == M-1):
        print(dist[y][x][z][b])
        break

    for i in range(4):
        wy = y+dy[i]
        wx = x+dx[i]
        if (wx >= 0 and wx < M and wy>=0 and wy < N):
            if(maze[wy][wx] == 0):
                if(dist[wy][wx][z][1-b] == 0):
                    dist[wy][wx][z][1-b] = dist[y][x][z][b] + 1
                    deq.append([wy,wx,z,1 - b])
            elif(maze[wy][wx] == 1 and z < K-1):
                if(dist[wy][wx][z+1][1-b] == 0):
                    if b == 0:
                        dist[wy][wx][z+1][1-b] = dist[y][x][z][b] + 1
                        deq.append([wy,wx,z+1,1 - b])
                    else:
                        dist[y][x][z][1-b] = dist[y][x][z][b] + 1
                        deq.append([y,x,z,1 - b])
else:
    print(-1)