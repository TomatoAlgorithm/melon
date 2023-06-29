import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()

def solution():
    n = int(input())
    
    card = deque()

    for i in range(n):
        card.append(i+1)
    
    for i in range(n-1):
        card.popleft()
        card.append(card.popleft())

    return card.pop()