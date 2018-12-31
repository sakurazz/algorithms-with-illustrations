# 394. Decode String


Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

## Idea

* 核心是  3 * “abc” 所以，要找到“abc” 的获取方式，以及触发 `times`的开关。
* 所以，用`[`和`]`, 作为**触发**开关，用`stack`存储“abc”。 

### Case 

```
"3[a]2[bc]"
"3[a2[c]]"
"2[abc]3[cd]ef"
```


## Code 

### 1. 2个stack 

``` python
# Time: O(n)? where n = len(s)
# Space: O(n) 
# 394. Decode String

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_content(letters):
            content = []
            char = letters.pop()
            while char != "[":
                content.append(char)
                char = letters.pop()
            return content[::-1], letters
                
        def get_times(left):
            times = []
            while left >= 0 and s[left].isdigit():
                times.append(s[left])
                left -= 1
            res = "".join(times[::-1])
            return int(res)
            
        letters = []
        brackets = []
        for i, char in enumerate(s):
            if not char.isdigit(): # [a]
                if char == "]":
                    left = brackets.pop()
                    time = get_times(left-1)
                    content, letters = get_content(letters) # [a]
                    for _ in range(time):
                        letters += content
                else: 
                    if char == "[":
                        brackets.append(i)
                    letters.append(char)
                    
        return "".join(letters)
```


### 2. 优化 stack 

``` python 
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i, char in enumerate(s):
            if char == "]":

                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()

                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                n = int(n)
                
                stack.append(n * sub)
            else:
                stack.append(char)
        return "".join(stack)
```

### 3. DFS

``` python 
class Solution(object):
    def __init__(self):
        self.i = 0
        
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.dfs(s)
    
    def dfs(self, s):
        content = []
        
        while self.i < len(s):
            if s[self.i].isdigit():
                n = ""
                while self.i < len(s) and s[self.i].isdigit():
                    n += s[self.i]
                    self.i += 1
                n = int(n)
            
            elif s[self.i] == "[":
                self.i += 1
                sub = self.dfs(s)
                content.append(n * sub)
                
            elif s[self.i] == "]":
                self.i += 1
                return "".join(content)
            
            else:
                content.append(s[self.i])
                self.i += 1
                
        return "".join(content)
        
```