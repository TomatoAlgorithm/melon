import sys

input = sys.stdin.readline

class trie_node:
    def __init__(self) -> None:
        self.isEnd = False
        self.link = {}

class Trie:
    def __init__(self) -> None:
        self._root = trie_node()

    def recurAdd(self, node:trie_node, word:str) -> None:
        if len(word) == 0:
            node.isEnd = True
            return
        
        ch = word[0]
        next_link = node.link.get(ch)
        if next_link is None:
            node.link[ch] = trie_node()
            next_link = node.link[ch]

        self.recurAdd(next_link, word[1:])

    def add(self, word:str) -> None:
        if len(word) == 0:
            return
        
        self.recurAdd(self._root, word)

    def recur_search(self, node:trie_node, word: str) -> bool:
        if len(word) == 0:
            return node.isEnd
        
        ch = word[0]
        next_link = node.link.get(ch)
        if next_link:
            return self.recur_search(next_link, word[1:])
        return False
        
    def search(self, word:str) -> bool:
        if len(word) == 0 :
            return True
        
        return self.recur_search(self._root, word)
    
    def searchPrefix(self, word:str) -> str:
        if len(word) == 0:
            return ''
        
        next_link = self._root
        
        for i in range(0, len(word)):
            ch = word[i]
            next_link = next_link.link.get(ch)
            if next_link:
                continue
            else:
                return word[:i+1]
        else:
            return word
    
trie = Trie()
name_set = {}

N = int(input())

for _ in range(N):
    nickName = input().strip()
    if nickName in name_set:
        name_set[nickName]+=1
        print(nickName+str(name_set[nickName]))
        continue
    else:
        name_set[nickName] = 1

    serverName = trie.searchPrefix(nickName)
    trie.add(nickName)
    print(serverName)