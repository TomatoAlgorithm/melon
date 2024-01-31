from collections import deque

N = int(input())

img = [list(input()) for _ in range(N)]
global dr, dc
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def find_rgb():
    global dr, dc
    cnt = 0
    visited = [([False]*N) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                que = deque()
                que.append([i,j,img[i][j]])
                
                while que:
                    row, col, color = que.popleft()
                    
                    for d in range(4):
                        nr = row+dr[d]
                        nc = col+dc[d]
                        if 0<=nr<N and 0<=nc<N and visited[nr][nc] == False and img[nr][nc] == color:
                            visited[nr][nc] = True
                            que.append([nr,nc,color])
                cnt+=1
                
    return cnt

correct = find_rgb()
for i in range(N):
    for j in range(N):
        if img[i][j] == 'G':
            img[i][j] = 'R'
incorrect = find_rgb()
print('{0} {1}'.format(correct, incorrect) )