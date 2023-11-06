import sys

def input():
    return sys.stdin.readline().rstrip()

sentences = []

def solution():
    global sentences
    brackets = input()

    couple = []
    newList = []

    for bIdx in range(len(brackets)):
        b = brackets[bIdx]
        if(b == '('):
            couple.append(bIdx)
        elif(b == ')'):
            newList.append((couple.pop(),bIdx))

    OXs = [True]*len(newList)

    dfs(0,OXs,newList,brackets)
    sentences.remove(brackets)
    sentences = list(set(sentences))
    sentences.sort()
    
    print(*sentences, sep='\n')


def dfs(depth, OXs, couple, sentence):
    global sentences
    if(depth == len(couple)):
        for i in range(len(OXs)):
            if(OXs[i] == False):
                for c in couple[i]:
                    sentence = sentence[:c] + '_' + sentence[c+1:]
        sentence = sentence.replace('_','')
        sentences.append(sentence)
        return
    
    for i in range(2):
        if(i==0):
            OXs[depth] = True
        else:
            OXs[depth] = False
        dfs(depth+1,OXs,couple,sentence)

solution()