import sys

def input():
    return sys.stdin.readline().rstrip()

def mySolution(n):
    c500 = n//500
    c100 = (n%500)//100
    c50 = ((n%500)%100)//50
    c10 = (((n%500)%100)%50)//10

    print(c500+c100+c50+c10)

def correctAnswer(n):
    count = 0
    # 큰 단위의 화펴부터 차례대로 확인
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin # 해당 화펴|로 거슬러 룰 수 있는 동전의 개수 세기
        n %= coin
    print(count)

n = int(input())

mySolution(n)
correctAnswer(n)