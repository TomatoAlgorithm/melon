import itertools
import sys

def input():
    return sys.stdin.readline().strip()

expression = input()

stack = []
pairs = []

for idx in range(len(expression)):
    if expression[idx] == '(':
        stack.append(idx)
    elif expression[idx] == ')':
        pairs.append((stack.pop(), idx))

comb = [i for i in range(len(pairs))]
all_comb = []
answer = set()
for i in range(1, len(pairs)+1):
    for c in itertools.combinations(comb, i):
        all_comb.append(c)
    
for comb in all_comb:
    ns = []
    for c in comb:
        for p in pairs[c]:
            ns.append(p)
    ns.sort(reverse=True)
    a = expression
    for n in ns:
        a = a[:n]+a[n+1:]
    answer.add(a)
answer = list(answer)
answer.sort()

print(*answer, sep='\n')