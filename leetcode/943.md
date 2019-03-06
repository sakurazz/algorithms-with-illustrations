# 943. Find the Shortest Superstring

* [ ] 是否可以用heap 优化 两两单词求overlap(） O(n^2)

Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

Example 1:

```
Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
```

Example 2:

```
Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
```

## 一个理想的思路

* 每次总是找最好的一对，拼完之后再放回去，迭代，直到只剩下一个string。但是有一个问题？ [❌]
* abc, bct的答案是 abct, distance(abc, bct) = 1, distance(bct, abc) = 3, 所以问题可以转换成旅行商问题(Travelling Salesman Problem) 

## Show me the code 

### 1. Wrong solution 

``` python 
# wrong answer 
class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        def overlap(w1, w2):
            """
            "abcd", "bcdef" -> 3, "abcdef"
            """
            n1, n2 = len(w1), len(w2)
            ans = 0
            s = ''
            for i in range(1, min(n1, n2) + 1):
                if w1[-i:] == w2[:i]:
                    if ans < i:
                        ans = i
                        s = w1 + w2[i:]
            for i in range(1, min(n1, n2) + 1):
                if w2[-i:] == w1[:i]:
                    if ans < i:
                        ans = i
                        s = w2 + w1[i:]
            return (ans, s) if ans > 0 else (ans, w1 + w2)
        
        A = set(A)
        # every time, choose two string that has have the best overlap degree
        while len(A) != 1:
            max_overlap_degree, joint_str = float('-inf'), None 
            str_A, str_B = None, None 
            
            for a, b in itertools.combinations(A, 2):
                overlap_degree, new_str =  overlap(a, b)
                if overlap_degree > max_overlap_degree:
                    max_overlap_degree, joint_str = overlap_degree, new_str
                    str_A, str_B = a, b 
            
            A.remove(str_A)
            A.remove(str_B)
            A.add(joint_str)
        return A.pop()
```

**wrong case:** 

```
["dnete","tef","ift","efd","fdn"]
```

correct answer: "iftef**dnete**"
					       			
wrong answer: "ift**dnete**fdn"

More information: check [greedy solution](https://leetcode.com/problems/find-the-shortest-superstring/discuss/195040/Greedy-solution-is-WRONG.-If-your-greedy-solution-gets-AC-it-only-means-you-are-LUCKY-enough.)

```
Explanation: 
iftefdnete
     dnete
  tef
ift 
   efd
    fdn	
---   
   efdnete
  tef   tef
ift
```

### 2. Correct solution 

``` python 
class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        def overlap(x, y):
            '''
            "abc", "bce": x[1:] == y[:3-1]
            We may assume that no string in A is substring of another string in A.
            '''
            for i in range(1, len(x)):
                if x[i:] == y[:len(x)-i]:
                    return len(x) - i
            return 0
             
        # 1. get overlap distance: overlap(abc, bce) = 2 
        dist = [[0]*len(A) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                dist[i][j]=overlap(A[i], A[j])

        # 2. 0101 -> 0111 : {['efd','tef']} + (tef →ift) >= ['efd', 'ift', 'tef']?    
        dp     = [[0]   *len(A) for _ in range(1<<len(A))] 
        parent = [[None]*len(A) for _ in range(1<<len(A))]
        
        for mask in range(1<<len(A)):
            for bit in range(len(A)):
                if not mask & (1<<bit): continue 
                # find "1" -> 0111
                pmask = mask ^ (1<<bit) # ->0101 by deleting "1" 
                if pmask == 0: continue
                # max(0011, 0101, 0110 -> 0111)
                for pbit in range(len(A)):
                    if pmask & (1<<pbit):
                        # {['efd','tef']} + (tef →ift) >= ['efd', 'ift', 'tef']
                        if dp[pmask][pbit] + dist[pbit][bit] >= dp[mask][bit]:
                            dp[mask][bit] = dp[pmask][pbit] + dist[pbit][bit]
                            parent[mask][bit] = pbit

        # 3. get the path: 3 fdn -> 2 efd -> 0 tef -> 1 ift
        mask = (1<<len(A)) - 1
        index = dp[mask].index(max(dp[mask]))

            # 3.1 index -> [1, 0, 2, 3] 
        word_order = []
        while index != None:
            word_order.append(index)
            index, mask = parent[mask][index], mask^(1<<index)
        word_list = word_order[::-1]
        
            # 3.2 [1, 0, 2, 3] -> [ift, ef, d, fdn]
        pre = word_list[0]
        res = [A[pre]]
        for _, cur in enumerate(word_list[1:]):
            start = dist[pre][cur]
            res.append(A[cur][start:])
            pre = cur

        return ''.join(res)
```


## Reference 

- [How to implement a dynamic programming algorithms to TSP in Python?](https://stackoverflow.com/questions/30114978/how-to-implement-a-dynamic-programming-algorithms-to-tsp-in-python)
- [4.7 Traveling Salesperson Problem - Dynamic Programming](https://www.youtube.com/watch?v=XaXsJJh-Q5Y)
- [code: step by step](https://repl.it/@WillWang42/tsp-943)