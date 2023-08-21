# (A + B) % p = ((A % p) + (B % p)) % p
# (A * B) % p = ((A % p) * (B % p)) % p
# (A - B) % p = ((A % p) - (B % p) + p) % p

# 팩토리얼 구하기

def originFact(n):
    res = 1
    for i in range(n):
        res *= (i+1)
    return res

def modularFact(n,m):
    res = 1
    for i in range(n):
        res = ((res % m) * (i % m))%m
    return res

print(originFact(100000000000000))
print(modularFact(100000000000000,10e9))