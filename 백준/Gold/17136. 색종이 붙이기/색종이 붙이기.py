from collections import deque

def square_check(row, col, board):
    max_size = 1

    for i in range(1,5):
        nr = row
        nc = col + i
        for r in range(2*(i+1) - 1):
            if not (0 <= nr < 10 and 0<= nc < 10 and board[nr][nc] == 1):
                return max_size
            
            if r < i:
                nr += 1
            elif r>=i:
                nc -= 1
    
        max_size += 1
    return max_size

board = [list(map(int, input().split(' '))) for _ in range(10)]
can_size = {}

for i in range(10):
    for j in range(10):
        if board[i][j] == 1:
            size = square_check(i,j,board)
            available = [i for i in range(size, 0, -1)]
            can_size[(i,j)] = available

remain_board = list(can_size.keys())
remain_board.sort(key=lambda x : (x[0], x[1]))
#remain_board = deque(remain_board)
remain_cnt = [5] * 5
global miv
miv = 1e9

def dfs(remain_board, remain_cnt):
    global miv
    if len(remain_board) == 0:
        miv = min(miv, 25 - sum(remain_cnt))
        return
    
    row, col = remain_board[0]

    for size in can_size[(row, col)]:
        if remain_cnt[size-1] > 0:
            new_remain_board = remain_board[:]
            new_remain_cnt = remain_cnt[:]
            new_remain_cnt[size-1] -= 1
            flag = True

            for nr in range(row, row+size):
                for nc in range(col, col+size):
                    try:
                        new_remain_board.remove((nr, nc))
                    except:
                        flag = False
            if flag:
                dfs(new_remain_board, new_remain_cnt)

dfs(remain_board, remain_cnt)
miv = miv if miv != 1e9 else -1
print(miv)