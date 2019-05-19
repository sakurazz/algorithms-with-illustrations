# Mind 

> 目标，计划，行动，反思

## To do 

ABCDEFGHIJKLMNOPQRSTUVWXYZ

- [x] Backtracking
- [ ] Complement: 补集思维
- [ ] Define: 261, 997, 1022(余数)
- [x] Edge case
- [ ] Fast and slow 
- [ ] Index/坐标视角: 283. Move Zeroes, 
- [x] Granularity|zoom out
- [ ] Limited states
- [ ] Math reduce: 49, 数学表达就是一种抽象
- [ ] Object: 418 
- [ ] Reverse thinking: 283. Move Zeroes(移非零)
- [x] Reduction
- [ ] Recursion
- [x] Sliding Window 
- [ ] safest way(greedy)
- [ ] 双标准: 678 
- [ ] 满足/不满足： 836 
- [ ] assume: 假设最优解，然后查看最优解的性质

--- 

- Edge case 
	- 1023 
	- [1033](https://leetcode.com/problems/moving-stones-until-consecutive/): edge case, `1,2,4` or `1,3,11` 识别出edge case题目就解出来了 
- Granularity
	- [815](https://leetcode.com/problems/bus-routes/): 将一个bus路线看作一个点，然后用BFS去做 
	- [918](https://github.com/willwang-x/algorithms-with-illustrations/blob/master/stories/granularity-zoom-out-918.md)
	- 1001 (preprocess)
	- [1031](https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/) subarray seen as a element 
	- [1049](https://leetcode.com/problems/last-stone-weight-ii/) all elements seen as two group
- [x] Safest way(greedy)
	- [942](https://leetcode.com/problems/di-string-match/): 最安全方法就是选最大，留有余地 
	- [31](https://leetcode.com/problems/next-permutation/): 找到decreasing subarray[...](https://leetcode.com/problems/next-permutation/solution/)
- [x] **Litmited** states: -> cycle -> hashmap 
	- [202](https://leetcode.com/problems/happy-number/): happy number，[Explanation](https://leetcode.com/problems/happy-number/discuss/56919/Explanation-of-why-those-posted-algorithms-are-mathematically-valid) 
	- [957](https://leetcode.com/problems/prison-cells-after-n-days/): 一共就365天
	- [1015](https://leetcode.com/problems/smallest-integer-divisible-by-k/): 同余且余数有限，会进入循环，所以第二次遇到相同余数，就进入循环了。
	- [1036](https://leetcode.com/problems/escape-a-large-maze/): 发现只有200个blocked pointer, 围城面积有限，从关注圈，变成关注点，如何跑出去。
- [x] **Reduction**: 把问题降维，从而用一个已知的解法解决。
	- LC 354 信封二维问题 可以转换成 一维的 LC300 longest sub sequence 
	- LC 1029, 二维比较，可以通过做差变成一维比较。
	- LC 85 二维求最大长方形，可以降为一维 成 LC84 
	- [LC 763](https://leetcode.com/problems/partition-labels/): valid sbtring, track所有字母的个数(多个) 变成 只 track index在最后的字母(1个)
	- [1035](https://leetcode.com/problems/uncrossed-lines/) uncrossed line 可以被reduced to `longest common subsequence`
	- [1049](https://leetcode.com/problems/last-stone-weight-ii/) 变成 knapsack 问题





## Reference 

* [How to Solve It](https://book.douban.com/subject/1456890/): [四步Image](https://www.douban.com/photos/photo/1691693211/)