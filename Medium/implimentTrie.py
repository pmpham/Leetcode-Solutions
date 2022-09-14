# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            if i in temp.children:
                temp = temp.children[i]
            else:
                temp.children[i] = Node()
                temp = temp.children[i]
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if i in temp.children:
                temp = temp.children[i]
            else:
                return False
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if i in temp.children:
                temp = temp.children[i]
            else:
                return False
        return True