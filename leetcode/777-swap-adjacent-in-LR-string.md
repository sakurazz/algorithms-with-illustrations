# 777. Swap Adjacent in LR String


In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.


```
Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
```

**Note:**

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.

## 想法

1. 基础情况是 LR的数量和个数应该是一样的。即去掉`X`后，是一样的。即LLLRRR。
2. 在有了LLLRRR的情况下，如何判断正确呢？困难！那么**反过来想**，什么情况会是错误的呢？(错误的情况判断完，那么剩下的就都是正确的了)
	* 如果start[i] = `L`, end[j] = `L`(第一个遇到的`L`), i < j, 必错。因为`L`只能往左移，这样永远不会和 end 对齐了。 e.g. [LXX, XLX] 
	* 如果start[i] = `R`, end[j] = `R`, i > j, 必错。 e.g. [XXR, XRX]


## Code 

``` python 
# Time: O(n)
# Space: O(1)

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """        
        i = j = 0
        if start.replace("X","") != end.replace('X',""):
            return False 
            
        for i, char in enumerate(start):
            if char != "X":
                while j < len(end) and end[j] == "X":
                    j += 1
                if char == "L": 
                    # LXX, XLX 
                    if i < j:
                        return False 
                else:
                    # XXR, XRX 
                    if i > j:
                        return False 
                j += 1
        return True    
```