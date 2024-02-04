N,M = map(int, input().split())
arr = list(map(int, input().split()))
C = [0]*M
S = [0]*N
S[0] = arr[0]
C[S[0]%M] += 1 
for i in range(1,N):
    S[i] = S[i-1]+arr[i]
    C[S[i]%M] += 1
    
answer = C[0]
for i in range(M):
    cnt = C[i]
    if cnt >= 2:
        answer += (cnt*(cnt-1))//2
        
print(answer)