# 1. 문제 접근 방식 => 구현 느낌으로 풀었음 / 문제가 설명하는데로 코딩했다.
# 2. 시간 복잡도 => N * M * 4
# 3. 질문 사항
# 4. 그 외에 나누고 싶은 것들

from collections import deque

N, M = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
board = []
visited = [[False for _ in range(M)] for _ in range(N)]

# board 
# 0 -> 청소되지 않은 칸
# 1 -> 벽
for _ in range(N):
    board.append(list(map(int,input().split(' '))))

# d
# 0 -> 북쪽 dx 0 dy -1
# 1 -> 동쪽 dx 1 dy 0
# 2 -> 남쪽 dx 0 dy 1
# 3 -> 서쪽 dx -1 dy 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

que = deque()
que.append([r, c, d])
clean = 0

while(len(que) > 0):
    [y, x, d] = que.popleft()
    
    if not visited[y][x]: # 현재 칸이 아직 청소 되지 않은경우
        clean +=1
        visited[y][x] = True
        
    for _ in range(4):# 4방향 중 청소되지 않은 곳이 있는지 확인
        # 반시계 방향으로 회전 => 현재 방향에서 -1
        d = d - 1 if d >= 1 else 3
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx >= 0 and nx < M and ny >= 0 and ny < N and not visited[ny][nx] and board[ny][nx] == 0:
            que.append([ny, nx, d])
            break
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if(nx >= 0 and nx < M and ny >= 0 and ny < N):
            if(board[ny][nx] == 1):
                break
            else:
                que.append([ny,nx,d])
    
print(clean)