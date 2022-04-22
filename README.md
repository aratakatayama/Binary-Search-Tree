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

### InOrder algorithm 
```py
def _inOrder(self, node):
    if node:
        yield from self._inOrder(node._left)
        yield node._value, node._count
        yield from self._inOrder(node._right)
```
Generator which performs an inorder traversal only if node is not empty. Inorder traversal should return the elements in the tree in ascending value order. 

### User methods
```py
def search(self, x):
    return self._search(self._root, x)
    
def insert(self, val):
    return self._insert(self._root, val)

def inOrder(self):
    yield from self._inOrder(self._root)
```

## Populating BST and Print Tree
The objective of the populateBST algorithm:
1. If the value is not in the tree, then create a new node a insert it in the right order
2. If the value already exists, then increment the reference count by 1

The objective of printTree algorithm:
1. Print the elements in ascending order

### Modifying the Search algorithm 
We can search to see if the desired node exists or not. However, in the previous implementation it would only return a True if it finds the value anywhere in the tree, and a False if it doesn't. The populateBST algorithm not only needs to know if the value exists, however which node the value is contained in, so it when finds it, the algorithm can increment the reference count of that particular value. In order to do this, the following modification in the search alogirthm can be done: 
```py
if node == None:
    return node, False # do not have to return node, however the return values must be consistent
elif x == node._value:
    return node, True
```
By returning the node containing value x, populateBST algorithm can easily know which node's reference count it should increment. 

### PopulateBST algorithm
```py
def populateBST(self, val):
    node, found = self.search(val)  # storing two values in variables
    if found:
        node._count += 1
    else: 
        self.insert(val)
```

### PrintTree algorithm
```py
def printTree(self):
    for x, c in self.inOrder():
        print(x, c)
```




