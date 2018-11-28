# Dynamic Programming  




## Study

- [Dynamic Programming – 7 Steps to Solve any DP Interview Problem](http://blog.refdash.com/dynamic-programming-tutorial-example/)

## Notes

Consider using DP whenever you have to **make choices** to arrive at the solution, specifically, when the solution relates to subproblems.

In addition to optimization problems, DP is also **applicable** to **counting and decision problems**—any problem where you can express a solution recursively in terms of the same computation on smaller instances.

Although conceptually DP involves recursion, often for efficiency the cache is **built "bottom-up"**, i.e., iteratively. [Problem 17.3].

To save space, **cache space** may be **recycled** once it is known that a set of entries will not be looked up again. [Problems 17.1 and 17.2]

Sometimes, **recursion may out-perform a bottom-up DP** solution, e.g., when the solution is found early or subproblems can be **pruned** through bounding. [Problem 17.5]


## Key words

- choice: 120, 97, 174, [221 Matrix], 903, **322**
- variable: 188, 474,
- sequence aligment: [300](https://leetcode.com/problems/longest-increasing-subsequence/description/) , 152
- shortest path: 
- counting: 96 
- string: 5 
- DFS -> DP: 139, 678, 464 

## Corner cases

