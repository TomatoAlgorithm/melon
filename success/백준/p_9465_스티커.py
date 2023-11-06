# 다이나믹 프로그래밍의 조건
# 1. 최적 부분 구조
# 2. 중복된 부분 문제


# 스티커는 2 * N 으로 이루어진 array로 되어있다.
# 변이 닿아 있는 스티커는 선택할 수 없다.

# 하나의 열에서 경우의 수를 보았을 때 ( j )
# 1. 0번째 행을 선택
# 2. 1번째 행을 선택
# 3. 행을 선택하지 않음

# Pattern(i,j) = i번째 열에서 j 패턴을 선택했을 때의 값
# Sum(i,j) = i번째 열에서 j 패턴을 선택했을 때의 i 까지의 최댓 값
# Sum(i,j){
#   i == 0 : arr[0]
#   else : arr[i] + Sum[i-1][k] (k는 양립되는 패턴 ex.0 번째 패턴일 경우 -> 1,2번째 패턴 값 선택가능)
# }

n = int(input())

for _ in range(n):
    m = int(input())
    arr = []
    dp = [[0 for _ in range(m)] for _ in range(3)]

    for _ in range(2):
        arr.append(list(map(int,input().split(' '))))


    dp[0][0] = arr[0][0]
    dp[0][1] = arr[1][0]
    dp[0][2] = 0

    for i in range(1,m):
        dp[0][i] = max(dp[1][i-1],dp[2][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-1],dp[2][i-1]) + arr[1][i]
        dp[2][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
    
    print(max(dp[0][m-1],dp[1][m-1],dp[2][m-1]))

    