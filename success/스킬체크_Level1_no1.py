def solution(topping):
    cnt = 0
    typeCnt = len(set(topping))

    for i in range(len(topping)//2+1, len(topping)):
        one = set(topping[:i])
        two = set(topping[i:])
        if(one > two):
            break
        if(len(one) == len(two)):
            cnt+=1

    for i in range(len(topping)//2, -1, -1):
        one = set(topping[:i])
        two = set(topping[i:])
        if(two > one):
            break
        if(len(one) == len(two)):
            cnt+=1
    return cnt

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))