# Trie 

![Trie](https://i.imgur.com/w7j1TTW.gif)

from https://moaazsidat.com/writings/2015/11/24/supercharging-react-with-immutablejs/

## Notes

Tries are special trees (prefix trees) that make searching and storing strings more efficient. Tries have many practical applications, such as conducting **searches** and providing **autocomplete**. It is helpful to know these common applications so that you can easily identify when a problem can be efficiently solved using a trie.

Sometimes preprocessing a dictionary of **words** (given in a list) into a trie, will improve the efficiency of searching for a word of length k, among n words. Searching becomes O(k) instead of O(n).

Be familiar with implementing, from scratch, a Trie class and its `add`, `remove` and `search` methods.

## Key words
- implement trie [208](https://leetcode.com/problems/implement-trie-prefix-tree/description/)
- search: 421 

## Corner cases

## Example

## Code


``` python 
# 208. Implement Trie (Prefix Tree)

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root 
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = '#'
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur:
                return False 
            cur = cur[c]
        if '#' in cur:
            return True
        return False 
                
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root 
        for c in prefix:
            if c not in cur:
                return False 
            cur = cur[c]
        return True 
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix) 
```
