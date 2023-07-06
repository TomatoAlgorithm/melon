n = int(input())
cnt = 0
board = [0]*n

def isValid(depth):
    for i in range(depth):
        if(board[i] == board[depth] or depth - i == abs(board[depth] - board[i])):
            return False
    return True

def dfs(depth):
    global cnt
    if(depth == n):
        cnt+=1
        return
    else:
        for i in range(n):
            board[depth] = i
            if isValid(depth):
                dfs(depth+1)
        

dfs(0)
print(cnt)