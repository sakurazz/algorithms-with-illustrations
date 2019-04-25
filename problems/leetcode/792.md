--- 
layout: post
title:  思路的诞生之时空权衡：预处理
tags:
- 思路的诞生
status: publish
type: post
published: true
---

<br>


>  “迨天之未阴雨，彻彼桑土，绸缪牖户。” ——《诗经·豳风·鸱号》

### 1. 问题是这样子的：

Given string S and a dictionary of words `words`, find the number of `words[i]` that is a subsequence of `S`.

```
Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
```

**Note:**
- All words in words and S will only consists of lowercase letters.
- The length of S will be in the range of [1, 50000].
- The length of words will be in the range of [1, 5000].
- The length of words[i] will be in the range of [1, 50].

### 2. 一个理想的思路是：

1.第一眼觉得是字符串匹配问题: 遍历Words，在S中调用字符串匹配算法(LC392)查找，然超时！
![暴力解法](https://i.imgur.com/qZLd7y4.gif)

2.问题来了：**如何降低时间复杂度呢？**
💡—— 预处理: 遍历一次Words，在S中查找，所以对S进行预处理, 使得查找时间更短

3.根据我们子串匹配算法判断，我们需求是，如word “acd”, 在S(adcacd)中，在匹配c后，我们想要知道S中c后面没有d, 所以可以结构化S，知道每一个字母的index。 像这样： {"a":[0，3],"c":[2,4],"d":[1,5]}

![预处理](https://i.imgur.com/4OOJre9.gif)

4.嗯，不错，这样我们得到，a:0, c:2, 下一个匹配只要找到d中有没有 >2 的Index了，如果有就返回True. 问题是S如果很长，“d”中的Index很多怎么办？**有序数列😀 —— 二分查找！**

5.其实，如果我们知道S中每一个字母，指向后面最近的26字母位置，那我们就可以O(1)完成定位了，匹配一个words时间从原来的`O(len(word)*log(len(S)/26)) ` 变成了`O(len(word))`，虽然用了原来的26倍空间，但是获得了更快的时间，棒！

![深度预处理](https://i.imgur.com/ca4iDze.gif)

6.嗯... 换一个**顺序**，如果我们遍历一遍S，在Words查找呢？像这样：

![深度](https://i.imgur.com/NZadrTV.gif)

**小结一下：**

所以我们看到有三种预处理方法，比较一下时间和空间复杂度：

1. **预处理S**, 以遍历words为主，在S中查找: `O(len(S) + len(words)*w*log(S/26))` & `O(len(S)) `
2. **深度预处理S**, 以遍历words为主，在S中查找: `O(len(S) + len(words)*w)` & `O(26len(S))`
3. **预处理words**，以遍历S为主，在words查找: `O(len(words) + len(S) + w*len(words))` & `O(len(words)*w)`

注: where w is average length of words

**升华一下：😇**

时空权衡，在**字符串**里，是**输入结构化**; 在**数据结构**上，**偏好散列法**; 在**设计思想**上，有**动态规划**; 在**工作**上，即**「台上一分钟，台下十年功」**; 所谓**准备的艺术**。

### 3. Show me the code:
<script src="https://gist.github.com/WillWang-X/93abbc71bd3fa09ea8425531044fff9b.js"></script>
### 4. 想多玩一会？
- [322. Coin Change](https://leetcode.com/problems/coin-change/description/) : 两层For循环，调换位置，看看有什么不一样。
- 时空权衡常见用途：计数法排序，字符串匹配，散列法，B树。
- 当我们在Google，输入关键词，得到文档列表时，Google引擎在做些什么呢？是在搜索所有文档，搜索这个关键词么？还是... 提醒：Inverted Index 

### 5. 感谢
- Master Zhao 
- Yingda Zhen 
- Anany: Introduction to the Design and Analysis of Algorithms (3rd, 2011): 第七章：时空权衡



<br>
<br>

简之           
2018.03.07           
VKC
