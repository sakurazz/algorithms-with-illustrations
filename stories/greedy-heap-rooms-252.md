# Greedy - Meeting roooms 252 



## 1. 问题是这样子的

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...]` (si < ei), find the minimum number of conference rooms required.


```
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
```

-- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/description/)




## 2. 一个理想的思路是

Key idea: If a new meeting **starts** while no meeting is **ended**, we need an additional room.

Thus, we can decide if we need an additional room by comparing a new meeting's start time with the end time of the meeting that ends earliest.

When it comes to find **just the one** that ends **earliest**, "Priority queue" always occurs to me. 

Therefore, if we have a `heap` that holds end time of the meeting that's in and a intervals that are **sorted** by the start time. 
Then, we can iterate the intervals and compare each meeting's start time with heap[0], if exists, to deicide if we need to add new interval's end time into our heap.

When meeting's start time < new interval's end time, we add it.
Otherwise, we pop the meeting in the heap and push the new meeting, which means the new meeting can use the just available room. 
Lastly, we can get the answer by just checking how much rooms we booked, that is the length of the heap.

Time Complexity:

* N is the length of the intervals.
* Sorting takes O(nlogn) and heap push and pop takes O(logn), 
* So the iterating part takes O(nlogn). 
* The total complexity takes O(nlogn).


## 3. Show me the code

``` python 
# Time: O(nlogn), where n = len(intervals) 
# cause sort takes O(nlogn), for loop takes O(n) and each heap operation takes O(nlogn) in the worst case.

# Space: O(n) 

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key = lambda intervals : intervals.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        return len(heap)     
```

## 4. 拓展

![bike问题](https://i.imgur.com/pRW43Sm.jpg)

上述的问题可以转换成：(抽象到具象，再到抽象的过程)

> 有三件房间，有一堆会议，问最多能安排多少会议？
> 
> Given `n` meetings represented by pairs `(start,end)` with `3` rooms, your task is to find the maximal number of meetings that we can have.



```
Input: [ [1, 10], [1, 6], [2, 8], [3, 5] ]
Output: 3
```

### 思路：

可以利用meeting room II的思路来解决这个问题。

1. 会议表示为`[start ,end]`, 以会议`start time`排序`Input data`。
2. 像Meeting roomII, 那样解题，多一个限制条件，就是如果len(heap) > 3，然后不再放入heap中，但是如果新的会议[next.start, next.end] 中，next.start < heap[0].end, 也替换掉heap[0]的会议，为后面的会议留出更好的空间。

``` 
----------
 --------------
 	----------------
 		--

``` 

### show me the code:

``` python 
# https://repl.it/@WillWang42/meeting-rooms
# need to be proved 

import heapq
def max_meetings(meetings):
  meetings.sort()
  heap = []
  start, end = 0, 1
  res = 0 
  for m in meetings:
    if heap and m[start] >= heap[0]:
      heapq.heapreplace(heap, m[end])
      res += 1
    else:
      if len(heap) < 3:
        heapq.heappush(heap, m[end])
        res += 1
      else:
        if m[end] < heap[0]:
          heapq.heapreplace(heap, m[end])
  return res 


test1 = [[1, 10], [1, 6], [2, 8], [3, 5]] # 3
test2 = [[1,10],[2,9],[3,7],[4,6],[6,11]] # 4
print(max_meetings(test2))

```