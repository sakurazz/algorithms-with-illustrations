# 347. Top K Frequent Elements


Given a non-empty array of integers, return the k most frequent elements.

Example 1:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

Example 2:

```
Input: nums = [1], k = 1
Output: [1]
```

Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Idea

## Code 

### 1. O(n + klogn)

``` python
# Time:  O(n + klogn) where n = len(nums)
# Space: O(n)
# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_nums = collections.Counter(nums)
        heap = [(-freq, num) for num, freq in freq_nums.items()]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
```

### 2. O(n + nlogk)

``` python
# Time:  O(n + nlogk) where n = len(nums)
# Space: O(n)
# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_nums = collections.Counter(nums)
        
        heap = []
        for num, freq in freq_nums.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) == k + 1:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)][::-1]
```

### 3. O(n + n + k) counting sort 

``` python 
# Time:  O(n + n + k) where n = len(nums)
# Space: O(n)
# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_freq = collections.Counter(nums)
        freq_nums = collections.defaultdict(list)
        
        for num, freq in num_freq.items():
            freq_nums[freq].append(num)

        res = []
        for freq in range(len(nums), 0, -1):
            if freq in freq_nums:
                res += freq_nums[freq]

        return res[:k]
                    
       
```