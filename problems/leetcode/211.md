# [928 Minimize Malware Spread II](https://leetcode.com/problems/add-and-search-word-data-structure-design/description/)

![](https://i.imgur.com/jPGuOvk.gif)


## 1. 问题是这样子的

Design a data structure that supports the following two operations:

```
void addWord(word)
bool search(word)
```

search(word) can search a literal word or a regular expression string containing only letters `a-z` or .. `A` . means it can represent any one letter.



```
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```


## 2. 一个理想思路是

看到单词搜索，想到`Trie`.

## 3. Show me the code 

``` python 
# Time : AddWord(word):O(n) where n = len(word), Search(word):O(n)
# Space: O(26^M) or (P)[worst case] where M = the longest, P = average length * the number of words
# 211. Add and Search Word - Data structure design


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False 

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_end = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False 
        self.dfs(node, word)
        return self.res 
    
    def dfs(self, node, word):
        if not word:
            if node.is_end:
                self.res = True 
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:]) 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```