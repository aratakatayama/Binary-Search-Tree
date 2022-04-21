# Binary-Search-Tree

## Linked List Implementation of BST

### Internal class Node
```py 
class __Node():
        """Private class only for class BST"""
        def __init__(self, v, c=1):  # ref count default value of 1
            self._value = v
            self._count = c
            self._left = None
            self._right = None
```
Each node in this BST will contain four fields; value, reference count of the value, the left child, and the right child. 

### Class BST 
Following is the linked list implementation of binary search tree. 

#### Constructor
```py 
class BST():

    """Linked List Implementation of Binary Search Tree"""

    # class Node goes here 
        
    def __init__(self):
        self._root = None
        self._size = 0
```
Constructor for this class will contain a field to indicate the root, and the size of the entire BST. 

#### Search algorithm
```py
# recursive implementation of search algorithm in BST
def _search(self, node, x):
    if node == None:
        return False 
    elif x == node._value:
        return True
    elif x < node._value:
        return self._search(node._left, x)
    else:
        return self._search(node._right, x)
```
As search algorithm should return a boolean, there are two base cases for returning True and False. The base case for returning False, is when the node is empty. If the node is empty, there is no way it is equivalent to value x which is the value being searched. Another base case, but returning True, is when that node contains the value x. If the node itself contains x, then it has found the desired value. If the root contains a bigger value than x, the algorithm will recurse on the left child of the node, and it will keep recursing until the root node contains the value x. If the value x is larger than the value in the root node, it will recurse on the right child until it finds the value.

### Insert algorithm 
```py
# recursive implementation of insert algorithm
def _insert(self, p, val):
    if val < p._value:
        if p._left:  # if p has a left child 
            self._insert(p._left, val)
        else:  # if p does has an empty left child, the tree has ran off and this is where we should insert the value 
            p._left = self.__Node(val)
            self._size += 1
    else: 
        if p._right:
            self._insert(p._right, val)
        else:
            p._right = self.__Node(val)
            self._size += 1                      
```
This helper method first checks if the value is smaller than the root or not. If it is, then we will recurse on the left child, and otherwise, recurse on the right child. The algorithm will keep recursing until it runs off the tree, and the location it runs off, is where the algorithm inserts the value. 

### inOrder algorithm 

