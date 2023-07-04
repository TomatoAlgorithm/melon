import sys

def input():
    return sys.stdin.readline().rstrip()

sentences = []

def solution():
    global sentences
    brackets = input()

    couple = []

    for bIdx in range(len(brackets)):
        b = brackets[bIdx]
        if(b == '('):
            couple.append(bIdx)
        elif(b == ')'):
            for i in range(len(couple)-1,-1,-1):
                    if (isinstance(couple[i],int)):
                         couple[i] = (couple[i],bIdx)
                         break

    OXs = [True]*len(couple)

    dfs(0,OXs,couple,brackets)
    sentences.remove(brackets)
    sentences = list(set(sentences))
    sentences.sort()
    for i in range(0,len(sentences)):
        print(sentences[i])


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