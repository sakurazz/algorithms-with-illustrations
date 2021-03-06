# Queue

![queue](https://i.imgur.com/VFhfyxe.png)

> A Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO)

## 基础知识

source: [wiki](https://www.wikiwand.com/en/Queue_(abstract_data_type))

In computer science, a queue is a collection in which the entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed. This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed. Often a peek or front operation is also entered, returning the value of the front element without dequeuing it. A queue is an example of a linear data structure, or more abstractly a sequential collection.

Queues provide services in computer science, **transport**, and **operations research** where various entities such as data, objects, persons, or events are stored and held to be processed later. In these contexts, the queue performs the function of a buffer.

## 典型应用

- queue + BFS

## 最佳实践

``` python
import collections

q = collections.deque([root,])
while q:
	# do sth.
```

## 木桩训练

- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/)
- [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)
- [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)


## Explain

## Q&A 

## More