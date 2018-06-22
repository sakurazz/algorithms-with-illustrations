# Bug-Free 指南

## 在哪里代码会出错？

1. **While loop **没有注意 `IndexError: list index out of range`: e.g. 349. Intersection of Two Arrays ![错误截图](https://i.imgur.com/fqejzC3.png)
2. 边界条件
	- 输入为空
	- `=` 条件： 如![57 insert intervals](https://i.imgur.com/Vu9HUA8.png) 
