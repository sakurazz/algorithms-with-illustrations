# Two pointers

![two pointers](https://jojozhuang.github.io/public/notes/algorithm-two-pointers/two_pointers.png)

by [Rong](https://jojozhuang.github.io/note/dsa/algorithm-two-pointers/)

## 基本知识

Two pointer is really an easy and effective technique which is typically used for searching pairs in a **sorted** arrays.

## 典型应用

- search **pairs** in a **sorted** arrays

## 最佳实践

- 2 sum pairs 

### two sum pairs

``` python
def two_sum(head, tail, target):
    combo = []
    while head < tail:
        sum_ = nums[head] + nums[tail]
        if   sum_ < target:  head += 1
        elif sum_ > target:  tail -= 1
        else:
            combo.append([nums[head], nums[tail]])
            head, tail = head+1, tail-1
            # avoid duplicate 
            while head < tail and nums[head] == nums[head-1]:
                head += 1
            while head < tail and nums[tail] == nums[tail+1]:
                tail -= 1
    return combo
```

Try: [15](https://leetcode.com/problems/3sum/), [18](https://leetcode.com/problems/4sum/)

## 木桩训练

- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
- [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
- [828. Unique Letter String](https://leetcode.com/problems/unique-letter-string/)

## Explain 

## Q&A

## More 