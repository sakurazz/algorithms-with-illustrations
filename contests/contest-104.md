
# Leetcode contest 104 

## 基石


### 总结：

* 914. X of a Kind in a Deck of Cards : 透过现象看本质，画图洞察得真知。
* 915. Partition Array into Disjoint Intervals: 学会定义关键词，一看得出如何比。
* 916. Word Subsets: 主次任务理清楚，核心问题看得出。
* 913. Cat and Mouse: 遇到选择想DP，假设已知想转移。
 
### 知识点：

- Analogy/Define/Assign/Prioritize
- 类比(Reduce to GCD)/ 定义(Compare min vs max in array)/分配(Focus on the baseline)/选择(DP : DFS with memo)

## 913. cat and mouse 

``` python 
# case: [[6],[4],[9],[5],[1,5],[3,4,6],[0,5,10],[8,9,10],[7],[2,7],[6,7]]

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

解决case过不了的问题：

``` python 
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