"""
몇 사 분면인지 찾아볼까?
2^N-1로 나눠봐
그럼 몇사분면인지 나오지
그리고 해당 분면의 시작 점이 나올거 아니야
그럼 시작 지점이 2^N-1 * 해당 분면
그리고 그 안에서 또 몇 사분면인지 찾아서 계산하면 됨 
"""

N, r, c = map(int, input().split(' '))
ans = 0
for k in range(N-1,-1,-1):
    v = r//2**k
    h = c//2**k

    if h==0 and v==0:
        continue
    elif h==1 and v==0:
        ans += 4**k
        c -= 2**k
    elif h==0 and v==1:
        ans += 4**k*2
        r -= 2**k
    elif h==1 and v==1:
        ans += 4**k*3
        r-=2**k
        c-=2**k


print(ans)