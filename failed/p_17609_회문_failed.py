import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())

    for i in range(n):
        statement = input().rstrip()

        for j in range(len(statement)//2):
            if(statement[j] != statement[-1-j]):
                for k in range(j, len(statement)//2):
                    newState1 = ''.join(statement[x] for x in range(len(statement)) if x != k)
                    newState2 = ''.join(statement[x] for x in range(len(statement)) if x != len(statement) - 1 -k)
                    if isPalindrome(newState1):
                        print(1)
                        break
                    elif isPalindrome(newState2):
                        print(1)
                        break
                else:
                    print(2)
                break
        else:
            print(0)

def isPalindrome(statement):
    for i in range(len(statement)//2):
        if(statement[i] != statement[-1-i]):
            return False
    else:
        return True

solution()