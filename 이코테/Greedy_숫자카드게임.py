import sys

def input():
    return sys.stdin.readline().rstrip()

def mySolution(mat):
    maxV = -1
    for idx, m in enumerate(mat, 0):
        maxV = max(min(m),maxV)

    print(maxV)

mat = []
n, m = map(int, input().split(' '))
for i in range(n):
    mat.append(list(map(int, input().split(' '))))

mySolution(mat)