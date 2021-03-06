# Data Structure 

<img src="https://i.imgur.com/OUh1FBf.png" alt="data structure mindmap" width="500"/> <br>
	
## To do 

* [ ] [CLASSIFICATION OF DATA STRUCTURE WITH DIAGRAM – DATA STRUCTURE NOTES
](https://www.csetutor.com/classification-of-data-structure-with-diagram/) : 图标
2. [Data Structures for  Coding Interviews](https://www.interviewcake.com/article/java/data-structures-coding-interview)
3. [The Technical Interview Cheat Sheet.md](https://gist.github.com/TSiege/cbb0507082bb18ff7e4b)
4. [Choosing the Right Data Structure to solve problems](http://careerdrill.com/blog/coding-interview/choosing-the-right-data-structure-to-solve-problems/)
5. [Data Structures — Diving Into Data Structures (Part 1)
](http://careerdrill.com/blog/coding-interview/choosing-the-right-data-structure-to-solve-problems/)
6. [Choosing the Right Collection](https://www.codeproject.com/Articles/1095822/Choosing-The-Right-Collection)
	
## 基本知识	
	
* **数据(Data)**:是客观事物的符号表示。在计算机科学中指的是所有能输入到计算机中并被计算机程序处理的符号的**总称**。
* **数据元素(Data Element)**:是数据的基本单位，在计算机程序中通常作为一个整体进行考虑和处理。
* **数据项**是数据的不可分割的最小单位。一个数据元素可由若干个数据项组成。
* **数据对象(Data Object)**：是性质相同的数据元素的集合。是数据的一个子集。
	
### 什么是数据结构？
	
* 定义1—- 是相互之间存在一种或多种特定关系的**数据元素的集合**。
* 定义2—- 按**某种逻辑关系组织**起来的一批数据（或称带结构的数据元素的集合）应用计算机语言并按一定的存储表示方式把它们存储在计算机的存储器中，并在其上定义了一个运算的集合。
	
### 数据存储结构(logic structure)
	
数据元素间抽象化的相互关系（简称为逻辑结构）。与数据的存储无关，独立于计算机，它是从具体问题抽象出来的数学模型。
	
#### 逻辑结构—划分方法一

* **线性结构**：有且仅有一个开始和一个终端结点，并且所有结点都最多只有一个直接前趋和一个后继。例如：线性表、栈、队列、串
* **非线性结构**：一个结点可能有多个直接前趋和直接后继。例如：树、图等。
	
#### 逻辑结构—划分方法二
	
* **集合结构**：数据元素之间未定义任何关系的松散集合。
* **线性结构**：数据元素之间定义了次序关系的集合（全序集合），描述的是**1对1**关系。
* **树形结构**：数据元素之间定义了层次关系的集合（偏序集合），描述的是**1对多**关系。
* **图状结构**：数据元素之间定义了网状关系的集合，描述的是**多对多**关系。
	
### 数据存储结构(physical structure)
	
> **存储结构（物理结构）**: 数据元素及其关系（数据的逻辑结构）在计算机存储器中的存储形式。是逻辑结构用计算机语言的实现，它依赖于计算机语言。
	
#### 说明
	
存储结构两方面的内容：
	
* （1）数据元素自身值的表示（数据域）
* （2）该结点与其它结点关系的表示（链域）
	
两种基本的存储方法：
	
* （1）顺序存储方法（顺序存储结构）
* （2）链接存储方法（链式存储结构）

同一种逻辑结构可采用不同的存储方法（以上两种之一或组合），这主要考虑的是运算方便及算法的时空要求。
	
* 顺序结构和链接结构适用在内存结构中。
* 索引结构和散列结构适用在外存与内存交互结构。
			
#### 3.1 顺序存储(Sequential)
	
使用一段**连续**的存储单元。优点：随机访问，查找速度快。缺点：**增删**效率低，大小固定。
	
在计算机中用一组地址连续的存储单元依次存储线性表的各个数据元素,称作线性表的顺序存储结构。
	
特点：

* 随机存取表中元素。
* 插入和删除操作需要移动元素。
	
#### 3.2 链式存储(Linked)
	
一组**任意**的存储单元。优点：大小动态扩展，增删效率高。缺点：不能**随机**访问。查找慢。
	
在计算机中用一组任意的存储单元存储线性表的数据元素(这组存储单元可以是连续的,也可以是不连续的)。它不要求逻辑上相邻的元素在物理位置上也相邻.因此它没有顺序存储结构所具有的弱点,但也同时失去了顺序表可随机存取的优点。
	
特点：
	
* 比顺序存储结构的存储密度小 (每个节点都由数据域和指针域组成，所以相同空间内假设全存满的话顺序比链式存储更多)。
* 逻辑上相邻的节点物理上不必相邻。
* 插入、删除灵活 (不必移动节点，只要改变节点中的指针)。
* 查找结点时链式存储要比顺序存储慢。
* 每个结点是由数据域和指针域组成。
	
#### 3.3 索引存储(Indexed)
	
e.g. LRU (linked list + hashmap)
	
在链式存储的基础上，通过附加的索引表标识数据元素存储地址（优点：查找速度快，缺点：占用更多存储 空间）
	
为了方便查找，整体无序，但索引块之间有序，需要额外空间，存储索引表。
	
除建立存储结点信息外，还建立附加的索引表来标识结点的地址。索引表由若干索引项组成。
	
特点：
	
* 索引存储结构是用结点的索引号来确定结点存储地址，
* 其优点是检索速度快，
* 缺点是增加了附加的索引表，会占用较多的存储空间。
* 在数据表中，就是用索引键来进行存储与检索的。
	
#### 3.4 散列存储(Hash)
	
通过散列技术保证查找速度的同时压缩存储空间，通过数据元素的散列值决定存储地址。选取某个函数，数据元素根据函数计算存储位置。
	
特点：
	
* 可能存在多个数据元素存储在同一位置，引起地址冲突。
* 优点：查找基于数据本身即可找到，查找效率高。存取效率高
* 缺点：存取随机，不便于顺序查找。
	
### 数据运算(Operation)
	
<img src="https://i.imgur.com/lLcuACt.png" alt="operation comparasion" width="400"/> <br>	

- 需要修改的图。(或者使用阵营九宫图)

<a href="http://bigocheatsheet.com/"><img src="https://i.imgur.com/62wQHWe.png" alt="data structure mindmap" width="600"/></a>

		

	
1. **Create**: 建立(Create)一个数据结构；
1. **Destroy**: 消除(Destroy)一个数据结构；
1. **Insert**: 把一个数据元素插入(Insert)到一个数据结构中；
1. **Delete**: 从一个数据结构中删除(Delete)一个数据元素；
1. **Search**: 对一个数据结构进行查找(Search)。
1. **Access**: 对一个数据结构进行访问(Access)；
1. **Modify**: 对一个数据结构(中的数据元素)进行修改(Modify)
1. **Sort**: 对一个数据结构进行排序(Sort)；
	
## 最佳实践 

### 如何选择数据结构？

- 数据量是否可知?
- 是否要求有序?
- pop顺序要求?
- 是否需要duplicate?
- 查找 vs 插入?
	- keys?	 

source: [In which scenario do I use a particular STL container?](https://stackoverflow.com/questions/471432/in-which-scenario-do-i-use-a-particular-stl-container)

![STL C++](https://i.stack.imgur.com/G70oT.png)
<br><br>

source: [未知]

![](https://i.imgur.com/qzdlGjB.jpg)
	
## 参考

1. 图片
	1. [数据结构mindmap](https://i.imgur.com/57TzYCD.png)
	1. [数据结构分类](https://i.imgur.com/UGaG1Ou.gif)
	1. [数据结构思维盗图](https://i.imgur.com/9OjiXaV.png) : https://www.xmind.net/m/f8sP/ 
	2. [数据结构mindmap](https://i.imgur.com/57TzYCD.png)
1. [数据，数据元素，数据结构](http://gotobenny.com/2018/02/25/2018-02-25-data-element-structure/) : 数据结构最少必要知识
1. [BigO cheatsheet](http://bigocheatsheet.com/) : 关于各种数据结构的介绍
1. [Data Structures — A Quick Comparison (Part 2)](https://medium.com/omarelgabrys-blog/data-structures-a-quick-comparison-6689d725b3b0) : 常用数据结构的优缺点
1. [Everything you need to know about tree data structures](https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c)
1. [Python Data Structures Tutorial](https://www.datacamp.com/community/tutorials/data-structures-python)
1. [ ] [图解图的存储结构](https://blog.csdn.net/wstz_5461/article/details/78290682)
1. [List of data structures](https://www.wikiwand.com/en/List_of_data_structures)
