# 트리의 높이 = h
# Data 개수 = n
# h = log(n)
# 원하는 숫자를 찾는 시간복잡도 -> log(n)

# 이진 탐색을 해야함

# 두 축구팀이 한 리그에서 넣은 골의 개수가 두개의 배열 형태로 주어집니다.
# 팀 베로니(teamB)가 진행한 각각의 경기에 대해서, 
# 팀 케로(teamK)가 획득한 골의 개수가 팀 베로니가 획득한 골의 개수보다 적거나 같은 경기 횟수를 계산하세요. 

# Example

# teamK = [1, 2, 3]
# teamB = [2, 4]
# team K는 3개의 경기를 뛰었고 각각 [1, 2, 3]개의 골을 넣었습니다.
# team B는 2개의 경기를 뛰었고 각각 [2, 4]개의 골을 넣었습니다.
# team B가 첫번째 경기에서 2 개의 골을 넣었기 때문에, team K가 1, 2 개의 골을 넣은 2 개의 경기가 해당됩니다.
# team B는 두번째 경기에서 4 개의 골을 넣었기 때문에, team K가 1, 2, 3 개의 골을 넣은 3 개의 경기가 모두 해당됩니다.
# 그러므로 최종 결과는 [2, 3]입니다. 

# Constraints
# 2 ≤ n, m ≤ 10e5
# 1 ≤ teamK[j] ≤ 10e9, where 0 ≤ j < n.
# 1 ≤ teamB[i] ≤ 10e9, where 0 ≤ i < m. 
# 단순하게 for 문을 두 번돌리면 (10e10 -> 10억이 넘어가서 알고리즘 시간이 초과됨)
# 이진 탐색을 사용해서 풀어야 함

def binarySearch(sortedArr, n):
    low = 0
    high = len(sortedArr)-1

    while(low <= high):
        mid = (high + low)//2
        
        if(n == sortedArr[mid]):
            low = mid
            high = mid
            break
        elif(n > sortedArr[mid]):
            low = mid + 1
        elif(n < sortedArr[mid]):
            high = mid - 1
    
    return low

teamK = [1, 4, 2, 4]
teamB = [3, 5]
teamK.sort()

for score in teamB:
    print(binarySearch(teamK, score))


