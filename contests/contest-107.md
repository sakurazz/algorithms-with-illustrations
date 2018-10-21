# Leetcode Weekly Contest 106

## 大观

* 925 Long Pressed Name: Space从O(n)做法，到O(1)边走边比较。
* 926 Flip String to Monotone Increasing: 空间从O(n)容易讲解，到O(1)二元了解  
* 927 Three Equal Parts: “相同”的定义，抽象的层次(计算，外在，个数)
* 928 Minimize Malware Spread II


**基石：**

*  [ ] Two pointer系列: 925 
*  [ ] Better interviewer 循序渐进讲解系列: 926 
*  [ ] 抽象的层次

## 925 Long Pressed Name

```
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```
```
1st idea: 
alex   [(a,1),(l,1),(e,1),(x,1)]
aaleex [(a,2),(l,1),(e,2),(x,1)]
```

思路是一个单词抽象出结构，然后再去比较结构。直观，容易写。

```python
# Time: O(n) where n = len(name)
# Space: O(n)
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        n = []
        def count(string):
            res = []
            cur, cnt = string[0], 1
            if len(string) == 1:
                return [(cur, cnt)]
            # "ssaaedd"
            for i in range(1, len(string)):
                if string[i] != cur:
                    res.append((cur,cnt))
                    cnt = 1
                else:
                    cnt += 1
                cur = string[i]
            res.append((cur, cnt))
            return res 
        
        a = count(name)
        b = count(typed)

        if len(a) != len(b):
            return False 
        for i in range(len(a)):
            if a[i][0] != b[i][0]:
                return False 
            if a[i][1] > b[i][1]:
                return False 
        return True

```
为了节省空间，可以直接边遍历边比较。在`typed`上走，`name`中有的就会消掉。如果全部消掉，如果这是y还没有走完，但是typed[j] != typed[j-1], 也返回False. 如 `x`, `xxxxxy`。 

```
Input: name = "leelee", typed = "lleeelee"

i
l  ee  l ee
ll eee l ee
j

Output: True 
------
Input: name = "saeed", typed = "ssaaedd"

s  a  ee d
ss aa e  ddx

Output: False 
```

```python 
# Time: O(n) where n = len(typed)
# Space: O(1)
class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif typed[j] != typed[j-1]: # or j == 0 (e.g. `x`, `yyy`)
                return False 
        return i == len(name)
```

## 926 Flip String to Monotone Increasing

```markdown
To find the boundary, 
how many `1` do we need to change at the **left** side? 
how many `0` do we need to change at the **right** side?
            -> count(1)
						0+	011233
							010110
							322111 +0
                                 <- count(0)

```
```python 
# Time: O(n)  where n = len(S)
# Space: O(n) 
class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        left_one = [0] * n
        right_zero = [0] * n
        
        # left to right: count 1
        tmp = 0
        for i in range(n):
            if S[i] == '1': tmp += 1
            left_one[i] = tmp
        left_one = [0] + left_one
        
        # right to left: count 0 
        tmp = 0
        for i in range(n-1, -1, -1):
            if S[i] == '0': tmp += 1
            right_zero[i] = tmp
        right_zero += [0]
        
        res = float("inf") 
        for i in range(n+1):
            res = min(res, left_one[i] + right_zero[i])
        return res 
```
上述想法，用O(1) Space实现，因为二元情形，不是0就是1

``` python 
# Time: O(n)  where n = len(S)
# Space: O(1) 
class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        S = "0"+ S # 11011 to 11111
        n = len(S)
        total_0s = S.count("0")
        nums1, nums0 = 0, 0
        res = float("inf")
        for i, num in enumerate(S):
            if num == "1": 
                nums1 += 1 
            else:
                nums0 += 1
            # "left: 1 to 0" + boundary + "right 0 to 1"
            res = min(res, nums1 + total_0s - nums0)
        return res 
```    

## 927 Three Equal Parts

这个题的启发：

* 如何定义“相同”,抽象的层次？ 数值相同(6 = 6)， 外形相同(110, 110), 结构相同(两个1，两个1)
* 从模糊相同到完全相同的渐进思路
* 相同以谁为参考呢？ 结尾那个为参考啊？因为尾部的`0`是固定的。

``` markdown 
start:
i           j            k
11011000000 110110000000 11011000
          i            j
          end

```

``` python 
# TLE: bad answer 
class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        string = "".join([str(A[i]) for i in range(len(A))])

        first = string[0]
        third = string[-1]
        second =string[1:-1]
                
        i, j = 0, len(A)-1
        while i+1 < j and first and second and third:
            fst = int(first, 2)
            trd = int(third, 2)
            if fst < trd:
                i += 1
                first += second[0]
                second = second[1:]
            elif fst > trd:
                j -= 1
                third = second[-1] + third 
                second = second[:-1]
            else:
                snd = int(second, 2)
                if fst == snd:
                    return [i, j]
                else:
                    j -= 1
                    third = second[-1] + third 
                    second = second[:-1]
        return [-1, -1]
```

```python 
# TLE: Bad answer
class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        if max(A) == 0:
            return [1,3]
        string = "".join([str(A[i]) for i in range(n)])
        i, j = 0, n-1
        while string[i] == '0':
            i += 1
        string = string.lstrip("0")
        first = string[0]  # 1
        second =string[1:-1] 
        third = string[-1]  # 1

        while i+1 < j and first and second and third:
            s_strip = second.lstrip("0")
            t_strip = third.lstrip("0")
            if first == t_strip:
                if t_strip == s_strip:
                    return [i, j]
                else:
                    j -= 1
                    third = second[-1] + third
                    second = second[:-1] 
            else:
                if len(first) != len(t_strip):
                    if len(first) < len(t_strip):
                        i += 1
                        first += second[0]
                        second = second[1:]
                    else:
                        j -= 1
                        third = second[-1] + third
                        second = second[:-1]
                else:
                    flag = True 
                    for i in range(len(first)):
                        if first[i] > t_strip[i]:
                            flag = False  
                    if flag:
                        i += 1
                        first += second[0]
                        second = second[1:]
                    else:
                        j -= 1
                        third = second[-1] + third
                        second = second[:-1]
        return [-1, -1]
```
```python
## deal with it in the whole way
class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        alen = len(A)
        string = "".join([str(i) for i in A])
        count_one = A.count(1)
        each_ones, remiander = divmod(count_one, 3)
        
        # edge cases 
        if remiander != 0: return [-1,-1]
        if each_ones == 0: return [0, 2]
        
        each_ending_0s = len(A) - len(string.rstrip("0"))
        
        first_tail, third_head = 0, 0 
        first_flag, third_flag = True, True 
        nums_1 = 0
        for i in range(alen-1, -1, -1):
            if A[i] == 1: nums_1 += 1
            if nums_1 == each_ones and third_flag:
                third_head = i 
                third_flag = False 
            if nums_1 == each_ones * 2 and first_flag:
                first_tail = i - 1
                first_flag = False 

        L_x_0s  = string[:first_tail+1].lstrip("0")
        M_x_0s  = string[first_tail+1:third_head]
        R_x_0s  = string[third_head:]
        
        L = L_x_0s.rstrip("0")
        M = M_x_0s.rstrip("0")
        R = R_x_0s.rstrip("0")
        
        diff_L = len(L_x_0s) - len(L) - each_ending_0s
        diff_M = len(M_x_0s) - len(M) - each_ending_0s
        
        if L != M or L != R: return [-1, -1]
        if diff_L < 0 or diff_M < 0: return [-1, -1]
        
        return [first_tail-diff_L, third_head-diff_M]
```