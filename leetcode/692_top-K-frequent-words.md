# 692. Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

```
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
```

Example 2:

```
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
```

Note:

* You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
* Input words contain only lowercase letters.

Follow up:

Try to solve it in O(n log k) time and O(n) extra space.

## Idea 

* top k -> 优先队列 -> maxheap or minheap 

问题：

* 排序不统一，(a,b), 优先排a, 重大到小，其次排b, 重小到大。用(-a, b) 或者(a, -b)  -> **overload** comparison operators

![int vs string](https://i.imgur.com/jNUVtbm.png)

### Edge case 

```
["i", "love", "leetcode", "i", "love", "coding"]
3
["aaa","aa","a"]
2
["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]
1
```

## Code 

### 1. maxheap: heapify，pop出前n个

``` python 
# Time: O(n + n + klogn) where n = len(words) 
# Space: O(n)

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_frequency = collections.Counter(words)        
        heap = [(-freq, word) for word, freq in word_frequency.items()]
        heapq.heapify(heap)
                        
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

### 2. minheap 确定下限，维持k个

```python
# Time: O(n + nlogk + klogk) where n = len(words) 
# Space: O(n)
'''
["i", "love", "leetcode", "i", "love", "coding"], k = 2
["i", "love"]

1. {"i":2, "love":2}
2. (2,i)

heap = {} with the size of 2 

e.g. 
["aaa","aa","a"]

'''
class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq.__lt__(other.freq)
        else:
            return self.word.__gt__(other.word)

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        # word frequency
        word_frequency = collections.Counter(words)
        
        # current k most frequent elements
        k_most_frequent = []
        for word, freq in word_frequency.items():
            heapq.heappush(k_most_frequent, Pair(freq, word))
            if len(k_most_frequent) == k + 1:
                heapq.heappop(k_most_frequent)
                
        return [heapq.heappop(k_most_frequent).word for _ in range(k)][::-1]
```

### 3. 类 counting sort O(n + n + klogk) 

``` python
# Time: O(n + n + klogk) where n = len(words) 
# Space: O(n)
# 692. Top K Frequent Words

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        word_frequency = collections.Counter(words)        
        
        freq_word = collections.defaultdict(list)
        for word, freq in word_frequency.items():
            freq_word[freq].append(word)
        
        res = []
        for freq in range(len(words), 0, -1):
            if freq in freq_word:
                for word in freq_word[freq]:
                    res.append((-freq, word))
            if len(res) > k:
                break
        
        res.sort()
        return [word for freq, word in res][:k]
                
            
        return [heapq.heappop(heap)[1] for _ in range(k)]
```