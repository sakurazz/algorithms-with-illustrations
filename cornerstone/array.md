# Array 

![quick sort](https://i.imgur.com/mWp1gdR.gif)

## Summary 

Array problems often have simple brute-force solutions that use 0(n) space, but subtler solutions that **use the array itself** to **reduce space** complexity to 0(1). [Problem 1]

Filling an array from the front is slow, so see if it's possible to **write values from the back**. [Problem 2]

Instead of deleting an entry (which requires moving all entries to its right), consider **overwriting** it. [Problem 5]

When dealing with integers encoded by an array consider **processing the digits from the back** of the array. Alternately, reverse the array so the **least-significant digit** is the first entry. [Problem 3]

Be comfortable with writing code that operates on **subarrays**. [Problem **10**]

It's incredibly easy to make **off-by-1** errors when operating on arrays. [Problems 4 and 17]

Don't worry about preserving the **integrity** of the array (sortedness, keeping equal entries together, etc.) until it is time to return. [Problem 5]

An array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing **a subset of** (0,1,..., W- 1]. (When using a Boolean array to represent a subset of (1,2,3,...,«}, allocate an array of size n+1 to simplify indexing.) [Problem 8].

When operating on 2D arrays, **use parallel logic** for rows and for columns. [Problem 17]

Sometimes it's easier to **simulate the specification**, than to analytically solve for the result. For example, rather than writing a formula for the i-th entry in the spiral order for an n X n matrix, just compute the output from the beginning. [Problems 17 and 19]

### Key word 

*  reduce space 
*  overwriting 
*  write values from the back
*  processing the digits from the back 
*  simulate the specification


## [Java API](https://i.imgur.com/VNGOnCx.png)

* Arrays
	* asList()
	* binarySearch(A, 641)
	* copyOf(A)
	* copyOFRange(A, 1, 5)
	* equals(A, B)
	* fill(A, 42)
	* find(A, 28)
	* sort(A)
	* sort(A, cmp)
	* toString() 
* ArrayList 
* List 
* `new int[]{1,2,3}` : allocating and initializating an array 
* `new Integer[3][]` : creates an array which will hold three rows, each of these must be explicitly assigned.

## 木桩训练

1. [75. Sort Colors](https://leetcode.com/problems/sort-colors/description/): 若干变种 ❤️
2. [mutiply two arbitrary-precision integers stored as Array](https://www.glassdoor.com/Interview/Given-2-very-large-numbers-each-of-which-is-so-large-it-can-only-be-represented-as-an-array-of-integers-write-a-function-QTN_266330.htm) ❤️
3. [Increment an arbitrary precision integer](https://fundatablog.wordpress.com/2016/07/11/problem-6-2-increment-an-arbitrary-precision-integer/)❤️
4. [55. Jump Game](https://leetcode.com/problems/jump-game/description/): Variant [45](https://leetcode.com/problems/jump-game-ii/description/) ❤️
5. [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) : Variant [80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/) ❤️
6. [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/): Variant: Write a program that takes an array of integers and finds the length of a longest subarray all of whose entries are equal.
7. [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)
8. [204. Count Primes](https://leetcode.com/problems/count-primes/description/) :  print all primes under N  ❤️
9. [Reorder an array according to given indexes](https://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/) Variant: Given an array A of integers representing a permutation, update A to represent the inverse permutation using only constant additional storage. 
10. [31. Next Permutation](https://leetcode.com/problems/next-permutation/description/)
	- Variant: Compute the fcth permutation under dictionary ordering, starting from the identity permutation (which is the first permutation in dictionary ordering).
	- Variant: Given a permutation p, return the permutation corresponding to the previous permutation of p under dictionary ordering.
11. Sample offline data
12. Sample online data 
13. Compute a random permutation
14. Cimpute a random subset
15. Cenerate nonuniform random numbers
16. [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/) 
17. [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/) ❤️
	* Variant: Given a sequence of integers P, compute a 2D array A whose spiral order is P. (Assume the size of P is n2 for some integer «.)
	* Variant: Write a program to enumerate the first n pairs of integers (a,b) in spiral order, starting from (0, 0) followed by (1, 0). For example, if n = 10, your output should be (0, 0), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (2, 1).
	* Variant: Compute the spiral order for an m X n 2D array A.
	* Variant: Compute the last element in spiral order for an m X n 2D array A in 0(1) time.
	* Variant: Compute the fcth element in spiral order for an mxn 2D array A in 0(1) time. 

18. [48. Rotate Image](https://leetcode.com/problems/rotate-image/description/)
	* Variant:Implement an algorithm to reflect A,assumed to be an nXn 2Darray,about the horizontal axis of symmetry. Repeat the same for reflections about the vertical axis, the diagonal from top-left to bottom-right, and the diagonal from top-right to bottom-left.
 	 
19. compute a row in pascal's triangle:  Compute the nth row of Pascal's triangle using 0(n) space. ❤️

