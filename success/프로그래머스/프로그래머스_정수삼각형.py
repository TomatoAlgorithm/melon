def solution(triangle):
    H = len(triangle)
    res = [[triangle[0][0]]] # 지금까지의 최대합 과 Max값을 저장하는 list
    for i in range(1, H):
        cur = []
        for j in range(i+1):
            me = triangle[i][j]
            meList = []
            if j == 0: # 첫 값
                cur.append(res[i-1][0] + me)
            elif j == i: # 끝 값
                cur.append(res[i-1][-1] + me)
            else: # 중간 값
                if res[i-1][j-1] < res[i-1][j]:
                    cur.append(res[i-1][j] + me)
                else:
                    cur.append(res[i-1][j-1] + me)
        res.append(cur)

    answer = -1
    
    for l in res[-1]:
        if l > answer:
            answer = l

    return answer