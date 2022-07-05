# https://leetcode.com/problems/implement-trie-prefix-tree/


# A trie (pronounced as "try") or prefix tree 
# is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
# There are various applications of this data structure, such as autocomplete and spellchecker.
# 참고: 
# 1. https://twpower.github.io/187-trie-concept-and-basic-problem 
# 2. https://velog.io/@gojaegaebal/210126-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8050%EC%9D%BC%EC%B0%A8-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0feat.-Class

import collections

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()


    # 삽입할 string 각각의 문자에 대해 자식 Node 를 만들며 내려간다. 
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children: 
                return False
            node = node.children[char] 

        return node.word # 만약 리프 노드가 아니라면! 정확히 일치하지 않으므로 False 
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True # 리프 노드가 아니어도, 모든 char 를 포함하고 있으므로 True

#---------------------------------------------#
#--------------- Other Answers ---------------# 
#---------------------------------------------#

# without default dict (it's confusing to me)
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word=False
        self.children={} # not default dict!
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node=self.root
        for i in word:
            if i not in node.children: # defaultdict 이 아니므로, 자식 노드에 없으면, 새로운 TrieNode() 를 추가하는 과정이 필요하다.
                node.children[i]=TrieNode()
            node=node.children[i]
        node.word=True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return node.word

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node=self.root
        for i in prefix:
            if i not in node.children:
                return False
            node=node.children[i]
        return True