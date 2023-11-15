# 1. 문제 접근 방식 => 방향을 정하고 나아가면서 오목체크하는 방식으로 구현
# 2. 시간 복잡도 => 19(가로) * 19(세로) * 5(오목 체크) * 4(방향)
# 3. 질문 사항
# 4. 그 외에 나누고 싶은 것들

global dx, dy, board
# 방향(4가지) : 오른쪽, 오른쪽 아래 대각선, 오른쪽 위쪽 대각선, 아래쪽
dx = [1, 1, 1, 0]
dy = [0, 1, -1, 1]
board = []

# 오목 찾기
def searchFive(c, y, x, d, cnt):# c => 색깔 / y,x => 좌표 / d => 방향 / cnt => 갯수 
    global dx, dy, board
    bx = x-dx[d]
    by = y-dy[d]
    # 첫돌의 반댓방향이 같은 돌이라면 안해도됨
    if cnt == 0 and not (bx < 0 or bx > 18 or by < 0 or by > 18) and board[by][bx] == c:  
        return False

    if board[y][x] == c:
        cnt += 1
    else:
        return False
    
    nx = x+dx[d]
    ny = y+dy[d]
    
    if (cnt == 5):
        if nx < 0 or nx > 18 or ny < 0 or ny > 18: # 5갠데 보드 끝이면
            return True
        else: # 육목 검사
            if board[ny][nx] == c:
                return False
            else:
                return True
            
    if not (nx < 0 or nx > 18 or ny < 0 or ny > 18):    
        return searchFive(c, ny, nx, d, cnt)


# Main
for i in range(19):
    board.append(list(map(int, input().split(' '))))

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            c = board[i][j]
            if(searchFive(c, i, j, 0, 0) 
            or searchFive(c, i, j, 1, 0) 
            or searchFive(c, i, j, 2, 0)
            or searchFive(c, i, j, 3, 0)):
                print(c)
                print('{0} {1}'.format(i+1, j+1))
                exit(0)
else:
    print(0)