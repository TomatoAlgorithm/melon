import sys

input = sys.stdin.readline

def check(nums):
    n = len(nums)
    dp = [([False] * n) for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True
        
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            dp[i][i+1] = True
            
    for k in range(2, n):
        for i in range(n-k):
            j = i+k
            if (nums[i] == nums[j]) and (dp[i+1][j-1]):
                dp[i][j] = True
    return dp

N = int(input())

nums = list(map(int, input().split(' ')))
dp = check(nums)

M = int(input())

for _ in range(M):
    s, e = map(int, input().split(' '))
    
    if dp[s-1][e-1]:
        print(1)
    else:
        print(0)  