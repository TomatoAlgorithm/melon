import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())

    for i in range(n):
        statement = input().rstrip()
        
        res = isPalindrome(statement)

        if res[0]:
            print(0)
        else:#여기가 핵심이였음 #유사 회문 구분할 때 안되는 부분부터 다시 검사했어야 했는데 그걸 놓쳤음
            newStatement = statement[res[1]+1:res[2]]
            res1 = isPalindrome(newStatement)
            if res1[0]:
                print(1)
            else:
                newStatement = statement[res[1]:res[2]-1]
                res = isPalindrome(newStatement)
                if res[0]:
                    print(1)
                else:
                    print(2)

def isPalindrome(statement):
    i = 0
    j = len(statement) - 1

    while i<=j:
        if statement[i] == statement[j]:
            i+=1
            j-=1
        else:
            return [False, i , j+1]
    else:
        return [True, -1, -1]



solution()