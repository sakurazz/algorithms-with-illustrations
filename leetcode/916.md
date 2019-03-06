
## 913. cat and mouse 


![看log找Bug](https://i.imgur.com/2WfskGM.jpg) 



## 0. 故事前传

913, 写完之后，自我感觉良好，逻辑清晰，代码好看。并写了一篇分享。直到被一个test case challenge了，

> [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]] 

觉得code逻辑没有问题，然后把整个DFS,打出来一步步check看看哪里出现了问题。

最后明白了几个道理:

* DFS遍历时，要注意有没有环的情况。
* 面试时，一定要多些几个test case. 
* 如果Interviewee challenge your solution and ask you to prove, 心态要端正，想想逻辑看似正确的solution, 也会是漏洞的。 
* Bottom up 比 top down 来的更扎实。

### 基石

- [ ] DFS与环
- [ ] Bottom up vs Top Down
- [ ] DFS 与 DP

## 1. 故事开始
```
Input: [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
Explanation:
4---3---1
|   |
2---5
 \ /
  0
```
-- [913. Cat and Mouse](https://leetcode.com/problems/cat-and-mouse/description/)

### 1.1 一个完美的错误答案

具体check我在leetcode上的分享[Clean Python code explained in detail](https://leetcode.com/problems/cat-and-mouse/discuss/176268/Clean-Python-code-explained-in-detail)

``` python 
# Wrong answer 
# failed cause the case: [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]

class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        self.graph = graph 
        self.memo = {}
        return self.move(2, 1, True)
        
    def move(self, cat, mouse, m_turn):
        key = (cat, mouse, m_turn)
        if key in self.memo:
            return self.memo[key]
        self.memo[key] = 0
        
        if m_turn:
            return self.mouse_play(key, cat, mouse, m_turn)
        else:
            return self.cat_play(key, cat, mouse, m_turn)
        
    def mouse_play(self, key, cat, turn, m_turn):
        # base case 
        for nxt in self.graph[turn]:
            if nxt == 0:
                self.memo[key] = 1
                return 1
        
        res = 2
        for nxt in self.graph[turn]:
            if nxt == cat:
                continue 
            tmp = self.move(cat, nxt, False)
            if tmp == 1:
                res = 1
                break
            if tmp == 0:
                res = 0
        self.memo[key] = res 
        return res 
    
    def cat_play(self, key, turn, mouse, m_turn):
        # base case 
        for nxt in self.graph[turn]:
            if nxt == mouse:
                self.memo[key] = 2
                return 2
            
        res = 1 
        for nxt in self.graph[turn]:
            if nxt ==0:
                continue 
            tmp = self.move(nxt, mouse, True)
            if tmp == 2:
                res = 2
                break 
            if tmp == 0:
                res = 0
        self.memo[key] = res 
        return res
```

## 1.2 错在哪里？

上面的解法问题，因为DFS会提前，决定一个`state`的状态，导致平局状态。

> For example, if mouse is one step away from the hole, and dfs picks another root before the hole root, if that root is a loop and return to this node again, dfs would think that's a draw(return to previous state) instead of mouse win.  —— Unicorn

对于Case: 

> [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]

![wrong answer](https://i.imgur.com/HLEZs3W.png)

 
Debug过程：https://repl.it/@WillWang42/cat-and-mouse-debug/

决定 `(9, 4, T)` 是 `(9, 1, F)` 和 `(9, 5, F)`, 如果先遍历`(9, 5, F)` 可以得到正确答案。但是如果先遍历 `(9, 1, F)`, 因为`DFS`过程会遇到`(7, 5, T)`,  被标记访问过，再继续`DFS`, 又遇到`(7, 5, T)` 这是会返回`0`, 导致`(9, 5, F)` 答案错误，而之后再访问`(9, 5, F)`, 因为之前存好了答案，导致不会深入，使得`(9, 4, T)`的答案也是错误的。

![](https://i.imgur.com/SoaTYNA.png)
![detail1](https://i.imgur.com/fhJwL66.png)
![detail2](https://i.imgur.com/H5tN79m.png)

## 1.3 有没有正确的DFS答案？

``` python
# revised version  provided by a friend
class Solution:
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        state = [[-1]*n for _ in range(n)]
        return self.search(state, graph, 1, 2)
    
    def search(self, state, graph, m_pos, c_pos):
        if state[m_pos][c_pos] != -1:
            return state[m_pos][c_pos]
        if m_pos == c_pos:
            state[m_pos][c_pos] = 2
            return 2
        if m_pos == 0:
            state[m_pos][c_pos] = 1
            return 1
        state[m_pos][c_pos] = 0
        
        all_cat_win = True 
        for nxt_mouse in graph[m_pos]:
            if nxt_mouse != c_pos:
                all_mouse_win = True 
                exist_cat_win = False 
                for nxt_cat in graph[c_pos]:
                    if nxt_cat != 0:
                        nxt_state = self.search(state, graph, nxt_mouse, nxt_cat)
                        if nxt_state != 1:
                            all_mouse_win = False 
                            if nxt_state == 2:
                                exist_cat_win = True 
                    if not all_mouse_win and exist_cat_win:
                        break 
                if all_mouse_win:
                    state[m_pos][c_pos] = 1
                    return 1
                if not exist_cat_win:
                    all_cat_win = False 
        state[m_pos][c_pos] = 2 if all_cat_win else 0
        return state[m_pos][c_pos]
```

## 1.4 更好的做法是?

为了避免上面的情况，我们可以从洞口开始标记每一个状态的答案。这样一定可以确保被标记完的状态一定正确。比如，如果离洞口最近所有点的状态(0, cat_postion, turn)都是返回**老鼠赢**. 所有( i , i,  turn) 都是返回**猫赢** 。

之后判断其他状态判断逻辑和minimax是一样的：

> The **Mouse player** will prefer `MOUSE` nodes first, `DRAW` nodes second, and `CAT` nodes last, and the Cat player prefers these nodes in the opposite order.


Thus, For mouse player, 

* If there is a child that returns `MOUSE wins`, then this node will go `MOUSE wins`.
* If all children that return `CAT wins`, then this node will return `CAT wins`.

然后再遍历`node`, 优先选择`node`的`degree`少，有点利用了拓扑排序的思想。

官网的Solution写得足够好, 就不献丑了。

``` python 
# Time:O(N^3), where N is the number of nodes in the graph. There are O(N^2) states, and each state has an outdegree of N, as there are at most N different moves.
# Space: O(N^2)
# https://leetcode.com/problems/cat-and-mouse/solution/

class Solution(object):
    def catMouseGame(self, graph):
        N = len(graph)

        # What nodes could play their turn to
        # arrive at node (m, c, t) ?
        def parents(m, c, t):
            if t == 2:
                for m2 in graph[m]:
                    yield m2, c, 3-t
            else:
                for c2 in graph[c]:
                    if c2:
                        yield m, c2, 3-t

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        # degree[node] : the number of neutral children of this node
        degree = {}
        for m in range(N):
            for c in range(N):
                degree[m,c,1] = len(graph[m])
                degree[m,c,2] = len(graph[c]) - (0 in graph[c])

        # enqueued : all nodes that are colored
        queue = collections.deque([])
        for i in range(N):
            for t in range(1, 3):
                color[0, i, t] = MOUSE
                queue.append((0, i, t, MOUSE))
                if i > 0:
                    color[i, i, t] = CAT
                    queue.append((i, i, t, CAT))

        # percolate
        while queue:
            # for nodes that are colored :
            i, j, t, c = queue.popleft()
            # for every parent of this node i, j, t :
            for i2, j2, t2 in parents(i, j, t):
                # if this parent is not colored :
                if color[i2, j2, t2] is DRAW:
                    # if the parent can make a winning move (ie. mouse to MOUSE), do so
                    if t2 == c: # winning move
                        color[i2, j2, t2] = c
                        queue.append((i2, j2, t2, c))
                    # else, this parent has degree[parent]--, and enqueue if all children
                    # of this parent are colored as losing moves
                    else:
                        degree[i2, j2, t2] -= 1
                        if degree[i2, j2, t2] == 0:
                            color[i2, j2, t2] = 3 - t2
                            queue.append((i2, j2, t2, 3 - t2))

        return color[1, 2, 1]
```