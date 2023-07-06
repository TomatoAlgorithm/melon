import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    sentences = input().split('.')

    for i in range(len(sentences)):
        sentence = sentences[i]
        cntA = 0
        cntB = 0
        trigger = False
        for k in range(len(sentence)//4,-1,-1):
            cntA = k
            n = len(sentence) - 4*k
            if(n % 2 == 0):
                trigger = True
                cntB = n//2
                break
        
        if(trigger == False):
            print(-1)
            return
        else:
            sentences[i] = 'AAAA'*cntA + 'BB'*cntB

    print(*sentences,sep='.')

solution()