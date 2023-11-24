from collections import deque

def solution(board):
    N = len(board)
    def isValid(nr, nc):
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
            return True
        return False
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    def canMove(cp): # 움직일 수 있는 방향을 return 하는 함수
        res = []
        
        for d in range(4): # 4방향 이동
            nr1 = cp[0][0] + dr[d]
            nc1 = cp[0][1] + dc[d]
            nr2 = cp[1][0] + dr[d]
            nc2 = cp[1][1] + dc[d]
            if isValid(nr1, nc1) and isValid(nr2, nc2):
                res.append([[nr1, nc1], [nr2,nc2]])

        for i in [-1,1]: # 회전
            state = abs(cp[0][0] - cp[1][0]) # 0 => 가로, 1 => 세로
            nr1 = cp[0][0] + i*(1-state)
            nc1 = cp[0][1] + i*state
            nr2 = cp[1][0] + i*(1-state)
            nc2 = cp[1][1] + i*state
            if isValid(nr1, nc1) and isValid(nr2, nc2):
                if i == -1:
                    res.append([[nr1,nc1],cp[0]])
                    res.append([[nr2,nc2],cp[1]])
                else: # 중복 체크 때문에 앞 뒤 순서가 유지되어야 함
                    res.append([cp[0], [nr1,nc1]])
                    res.append([cp[1], [nr2,nc2]])
                    
        return res
    
    que = deque()
    duplicate = []
    start = [[0,0],[0,1]]
    que.append([start, 0])
    duplicate.append(start)
    
    while que:
        cp, cnt = que.popleft()
        
        if (cp[0][0] == N-1 and cp[0][1] == N-1) or (cp[1][0] == N-1 and cp[1][1] == N-1):
            return cnt
        
        for move in canMove(cp): # 갈 수 있는 방향 중 중복이 아니라면 que 삽입
            if move not in duplicate:
                duplicate.append(move)
                que.append([move, cnt+1])
    
board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))