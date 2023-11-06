from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    dic = Counter(tangerine)
    dic.most_common()

    for d in dic.most_common():
        answer+=1
        k -= dic[d[0]]
        if(k <= 0):
            break

    return answer