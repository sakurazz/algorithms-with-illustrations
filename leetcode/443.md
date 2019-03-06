# 443. String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:
```
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 ```

Example 2:

```
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
``` 

Example 3:

```
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
```

Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.


## Idea

* 保持一个compress之后的subarray, 如何添加新的substring。 模拟之后手动写的过程就可以了。


## Code 

### 1.0 

``` python 
# Time: O(n)
# Space: O(1)
# 443. String Compression

"""
["a","a","b","b","c","c","c","d","e","e"]
                              i 
["a","2","b","2","c","3","d","e","e","e"]
                                      j
"""
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last, count = 0, 0

        def count2str(last, count):
            count_str = str(count)
            for j in range(len(count_str)):
                last += 1
                chars[last] = count_str[j]
            return last 
        
        for i in range(len(chars)):
            if chars[i] != chars[last]:
                if count > 1:
                    last = count2str(last, count)
                    last += 1
                    chars[last] = chars[i] 
                else: 
                    last += 1
                    chars[last] = chars[i]
                count = 1   
            else:
                count += 1
        
        if count > 1:
            last = count2str(last, count)
        
        return last+1

```

### 2.0 正向移动：展望

参考: 命名好read/write/anchor ，以及减少了一个变量

write: 指向下一个要写的地方。
read: 显示当前要读的地方。

``` python
# Time: O(n)
# Space: O(1)
# 443. String Compression

"""
["a","a","b","b","c","c","c","d","e","e"]
                              i 
["a","2","b","2","c","3","d","e","e","e"]
                                      j
-----------------------------------------
  0   1   2  3    4   5   6   7   8   9
          w 
["a","2","b","b","c","c","c","d","e","e"]
              r
          a
"""
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        anchor = write = 0 
        for read, char in enumerate(chars):
            if read + 1 == len(chars) or chars[read+1] != char:
                chars[write] = chars[anchor] 
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write
                
        
```