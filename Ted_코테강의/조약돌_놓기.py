# • 3×N 테이블의 각 칸에 양 또는 음의 정수가 기록되어 있다
# • 조약돌을 놓는 방법 (제약조건)
# - 가로나 세로로 인접한 두 칸에 동시에 조약돌을 놓을 수 없다
# - 각 열에는 적어도 하나 이상의 조약돌을 놓는다
# • 목표: 돌이 놓인 자리에 있는 수의 합을 최대가 되도록 조약돌을 놓는다

# 1열에 조약돌을 놓을 수 있는 방법( j )
# 1. 0
# 2. 1
# 3. 2
# 4. 0,2

# Pij = i 번째에 j 패턴으로 돌을 놓았을 때 획득 가능한 정수
# Sij = i 번째에 j 패턴으로 돌을 놓았을 때 i 까지 획득 가능한 최대 정수

# Sij {
#     Pij (i==0)
#     S(i-1)k + Pi(1,2,3,4) (k는 j와 양립가능한 패턴)
# }

def solution(arr, n):
    peb = [[0 for _ in range(4)] for _ in range(n)] 
    dp = [[0 for _ in range(4)] for _ in range(n)]

    for i in range(n):
        peb[i][0] = arr[0][i]
        peb[i][1] = arr[1][i]
        peb[i][2] = arr[2][i]
        peb[i][3] = arr[0][i] + arr[2][i]

    for i in range(4):
        dp[0][i] = peb[0][i]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1],dp[i-1][2]) + peb[i][0]
        dp[i][1] = max(dp[i-1][0],dp[i-1][2],dp[i-1][3]) + peb[i][1]
        dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + peb[i][2]
        dp[i][3] = dp[i-1][1] + peb[i][3]

    return max(dp[n-1][0],dp[n-1][1],dp[n-1][2],dp[n-1][3])

n=4
arr = [ [5,2,-1,3],
    [-1,8,-5,0],
    [2,3,12,7], ]

print(solution(arr, n))