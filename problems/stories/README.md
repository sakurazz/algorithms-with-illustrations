# Stories 

## To do 

* [压缩算法的通俗解释：deflate 算法](http://www.codersnotes.com/notes/elegance-of-deflate/) : 压缩是最常用的功能之一，压缩算法一般分成两大类：基于熵的压缩和基于字典的压缩。本文简单解释这两类算法的原理，以及将它们合在一起的 deflate 算法。
* [Beating hash tables with trees? The ART-ful radix trie](https://www.the-paper-trail.org/post/art-paper-notes/) : Tries are an unloved third data structure for building key-value stores and indexes, after search trees (like B-treesand red-black trees) and hash tables. 
	* This is where the Adaptive Radix Tree (ART) comes in. In this breezy, easy-to-read paper, the authors show how to reduce the memory cost of a regular radix trie by adapting the data structure used for each node to the number of children that it needs to store. In doing so they show, perhaps surprisingly, that the amount of space consumed by a single key can be bounded no matter how long the key is.