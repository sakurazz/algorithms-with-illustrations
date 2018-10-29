# Greedy - Stay ahead | induction


> we ensure that our resource becomes free as soon as possible while still satisfying one request. In this way we can maximize the time left to satisfy other requests.
> 
> —— *Algorithm Design* 


## Question 

```
input = [[0,6], [7, 8], [0,1] [1,3], [4, 5], [7, 9], [0, 2], [2, 4], [4, 7]]
output: 4 
Explanation:
------------ --
-- ---- ---  ----
----- -- ----
```

![algorithm design p119](https://i.imgur.com/mEstxT1.png)

## Intuition and Prove 

We ensure that our resource becomes free as soon as possible while still satisfying one request. In this way we can maximize the time left to satisfy other requests.

### Prove 

`A` is the greedy set and  `O` is the set of the optimal solution.

len(A) = k, len(O) = m

We prove that `k == m` by **induction**. 

* A[0][end]   <=  O[0][end]
* A[i-1][end] <=  O[i-1][end] where i >= 1
* Thus, A[i][end] <=  O[i][end]  

Then we will prove the statement by contradiction. f `Ans` is not optimal, then an optimal set `O` must have more requests, that is, we must have m > k. By prove, we have `A[i][end] <=  O[i][end]`. Since m > k, there is a request O[i+1] in `O`. Thus, `A` can have O[i+1], too.

## 拓展


> 有三件房间，有一堆会议，问最多能安排多少会议？
> 
> Given `n` meetings represented by pairs `(start,end)` with `3` rooms, your task is to find the maximal number of meetings that we can have.



```
Input: [ [1, 10], [1, 6], [2, 8], [3, 5] ]
Output: 3
```

### 思路：

同理如上，尽可能留有余地给之后的房间：

1. 以结束时间排序，这样可以更快让出房间, 给后面的**时间段**。
1. 新会议安排时，选择最晚结束会议的空房间，给后面的**更早开始的会议**的流油余地。


``` 
1 ----
2  --------------
3   	----------------
4  		          -----------  #  case two: chose 2 first, leave room 1 for meeting 5  
5  		  ----------------------        
``` 

### show me the code:

``` python 
# https://repl.it/@WillWang42/meeting-rooms

def max_meetings(meetings):
  start, end = 0, 1
  meetings.sort(key = lambda i: i[end])
  rooms, count = [0, 0, 0], 0
  
  for meeting in meetings:
    valid_time, room_id = -1, -1
    
    for i, endtime in enumerate(rooms):
      if endtime <= meeting[start] and valid_time <= endtime:
        valid_time = endtime
        room_id = i
        
    if room_id != -1:    
      rooms[room_id] = meeting[end]
      count += 1
      print(rooms)
      
  return count 
```

## Thanks

- [Greedy stays ahead 证明](https://www.cs.oberlin.edu/~asharp/cs280/2012sp/handouts/greedy_ahead.pdf)
- 《Algorithm Design》