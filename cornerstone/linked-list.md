
# Linked list 

* [ ] 将《element》中的习题整理出来。



![linked list](https://i.imgur.com/xwQ842u.png)

> A linked list is a linear data structure, the elements are not stored **at contiguous memory locations**. The elements in a linked list are linked using **pointers**.

## 基础知识

List problems often have a simple brute-force solution that uses 0(n) space, but a subtler solution that uses **the existing list nodes** to reduce space complexity to 0(1). 

Very often, a problem on lists is conceptually simple, and is more about **cleanly coding what's specified**, rather than designing an algorithm.

Consider using **a dummy head** (sometimes referred to as a sentinel) to avoid having to check for empty lists. This simplifies code, and makes bugs less likely. 

It's easy to forget **to update next** (and previous for double linked list) for the head and tail.

Algorithms operating on singly linked lists often benefit from using **two iterators**, one ahead of the other, or **one advancing quicker than the other**. 
 
## 典型应用


- deletion O(1): moditfy the value or pointer 
- dummy node: [2](https://leetcode.com/problems/add-two-numbers/description/)
- reverse: [25](https://leetcode.com/problems/reverse-nodes-in-k-group/description/), [92](https://leetcode.com/problems/reverse-linked-list-ii/description/), [206](https://leetcode.com/problems/reverse-linked-list/description/)
- partition: merge two lists
- linked list ~= array 
- two pointer (fast/slow pointers)
	- get the kth from last node 
	- detect cycle 
	- getting the middle node 

### Corner cases
- Single node 
- Two nodes
- Linked list has cycle. Clarify with the interviewer whether there can be a cycle in the list. Usually the answer is no.

## 最佳实践

- create
- insert
	- 1) At the front of the linked list.
	- 2) After a given node.
	- 3) At the end of the linked list.
- delete
- sort 

### Create 

``` python 
# Node class 
class Node: 
  
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
# Linked List class 
class SLinkedList: 
    
    # Function to initialize the Linked List object 
    def __init__(self):  
        self.head = None


list1 = SLinkedList()
list1.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.head.next = e2

# Link second Node to third node
e2.next = e3
```

## [Insert](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/)

A node can be added in three ways:

* 1) At the front of the linked list.
* 2) After a given node.
* 3) At the end of the linked list.


1) At the front of the linked list.
![head](https://i.imgur.com/idBfQcO.png)

``` python 
# This function is in LinkedList class 
# Function to insert a new node at the beginning 
def push(self, new_data): 
  
    # 1 & 2: Allocate the Node & 
    #        Put in the data 
    new_node = Node(new_data) 
          
    # 3. Make next of new Node as head 
    new_node.next = self.head 
          
    # 4. Move the head to point to new Node  
    self.head = new_node 
```

Time complexity of push() is O(1) as it does constant amount of work.


2) After a given node.

![a given node](https://i.imgur.com/JCUjiTr.png)

``` python 
# This function is in LinkedList class. 
# Inserts a new node after the given prev_node. This method is  
# defined inside LinkedList class shown above */ 
def insertAfter(self, prev_node, new_data): 
  
    # 1. check if the given prev_node exists 
    if prev_node is None: 
        print "The given previous node must inLinkedList."
        return
  
    #  2. Create new node & 
    #  3. Put in the data 
    new_node = Node(new_data) 
  
    # 4. Make next of new Node as next of prev_node  
    new_node.next = prev_node.next
  
    # 5. make next of prev_node as new_node  
    prev_node.next = new_node 
```

3) At the end of the linked list.

![end](https://i.imgur.com/YdKjP8R.png)

``` python 
# This function is defined in Linked List class 
# Appends a new node at the end.  This method is 
#  defined inside LinkedList class shown above */ 
def append(self, new_data): 
 
   # 1. Create a new node 
   # 2. Put in the data 
   # 3. Set next as None 
   new_node = Node(new_data) 
 
   # 4. If the Linked List is empty, then make the 
   #    new node as head 
   if self.head is None: 
        self.head = new_node 
        return
 
   # 5. Else traverse till the last node 
   last = self.head 
   while (last.next): 
       last = last.next
 
   # 6. Change the next of last node 
   last.next =  new_node 
```

### Delete

![delete](https://i.imgur.com/hoNrILV.png)

``` python 
# Given a reference to the head of a list and a key, 
# delete the first occurence of key in linked list 
def deleteNode(self, key): 
      
    # Store head node 
    temp = self.head 
  
    # If head node itself holds the key to be deleted 
    if (temp is not None): 
        if (temp.data == key): 
            self.head = temp.next
            temp = None
            return
  
    # Search for the key to be deleted, keep track of the 
    # previous node as we need to change 'prev.next' 
    while(temp is not None): 
        if temp.data == key: 
            break 
        prev = temp 
        temp = temp.next 
  
    # if key was not present in linked list 
    if(temp == None): 
        return 
  
    # Unlink the node from linked list 
    prev.next = temp.next
    temp = None 
``` 

### Sort 

[147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/description/)

## Explain

## Q&A

## Thanks 

