# 앙몬드에게 정수형 배열 arr, indexes 와 정수 X 가 주어집니다.
# 각 i 번째 indexes 항목에 대해, arr 에서 indexes[i] 번째 X 가 발생한 인덱스를 배열로 반환하세요.
# indexes[i] 번째 항목이 존재하지 않는 경우 해당 결과는 -1 입니다. 
# 주의: 반환될 배열은 1부터 시작되는 인덱싱(1-based indexing)이어야 합니다. 

# Example

# X = 8
# arr[n] = [1, 2, 20, 8, 8, 1, 2, 5, 8, 0]
# indexes[m] = [100, 2]

# Dict에 String key가 들어갈 때 로직
# String 을 Hash Function을 사용해 정수형으로 바꾸고 Memory에 저장


# Mine
def mySolution():
    X = int(input())
    arr = list(map(int,input().split(' ')))
    indexes = list(map(int,input().split(' ')))

    dict = {}
    k=0

    res = []

    for idx, a in enumerate(arr, 1):
        if a == X:
            k+=1
            dict[k] = idx

    for idx in indexes:
        res.append(-1 if not dict.__contains__(idx) else dict[idx])

    print(*res,sep='\n')

# Answer
def solution():
    X = 8
    arr = [1, 2, 20, 8, 8, 1, 2, 5, 8, 0]
    indexes = [100, 2]

    answer = {}
    k=0

    for i in range(len(arr)):
        if arr[i] == X:
            k+=1
            answer[k] = i+1

    for i in range(len(indexes)):
        try:
            print(answer[indexes[i]])
        except:
            print(-1)

solution()