INF = 1000000000
N = int(input())

W = [list(map(int, input().split(' '))) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(pre, bit):
    if bit == 2**N-1:
        if W[pre][0] != 0 :
            return W[pre][0]
        else:
            return INF
    if dp[pre][bit] != -1:
        return dp[pre][bit]
    
    dp[pre][bit] = INF

    for i in range(N):
        if (bit & (1 << i)) == 0 and W[pre][i] != 0:
            dp[pre][bit] = min(dp[pre][bit], dfs(i, bit | (1 << i))+W[pre][i])
    
    return dp[pre][bit]

print(dfs(0,1))