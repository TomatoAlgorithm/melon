def solution(sticker):
    N = len(sticker)

    if N == 1 : return sticker[0]

    # 처음걸 떼는지 안떼는지로 경우를 나눔
    dp_s = [ 0 for _ in range(N)]
    dp_e = [ 0 for _ in range(N)]
    dp_s[0] = sticker[0]

    if(N >= 2):
        dp_s[1] = sticker[0] # 처음 걸 뗐다면 2번째 건 뗄 수 없음
        dp_e[1] = sticker[1]

    # 처음 걸 뗐을 때 마지막 건 뗄 수 없기 때문에 마지막 전까지만 계산
    for i in range(2,N-1):
        dp_s[i] = max(sticker[i] + dp_s[i-2], dp_s[i-1])

    for i in range(2,N):
        dp_e[i] = max(sticker[i] + dp_e[i-2], dp_e[i-1])

    # N-1번째(마지막을 뗐다면 N번째) dp 값이 Max값임
    return max(dp_s[N-2], dp_e[N-1])