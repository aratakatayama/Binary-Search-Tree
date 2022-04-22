# Created by Arata Katayama 04/18/2022
# Lab 8 - Popularity with trees

class BST():

    """Linked List Implementation of Binary Search Tree"""

    class __Node():
        """Private class only for class BST"""
        def __init__(self, d, c=1):  # ref count default value of 1
            self._domain = d
            self._count = c
            self._left = None
            self._right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def _search(self, node, x):  # recursive implementation of search
        """Search algorithm for binary search tree"""
        if node == None:  # base case for False
            return node, False
        elif x == node._domain:  # base case for True
            return node, True
        elif x < node._domain:
            return self._search(node._left, x)
        else:
            return self._search(node._right, x)

    def _insert(self, p, val):
        """Helper function for inserting val in a tree rooted at p"""
        if val < p._domain:
            if p._left:   # if p._left is not None
                self._insert(p._left, val)
            else:
                p._left = self.__Node(val)  # left child = new inserted node
                self._size += 1
        else:
            if p._right:
                self._insert(p._right, val)
            else:
                p._right = self.__Node(val)
                self._size += 1

    def _inOrder(self, node):
        # yield is used without destroying the state of its local variable
        if node: # else if node is empty do nothing
            yield from self._inOrder(node._left)
            yield node._domain, node._count
            yield from self._inOrder(node._right)

    def search(self, x):  # public function for search
        return self._search(self._root, x)

    def insert(self, val):  # public function for insert
        if self._root:
            return self._insert(self._root, val)
        else:
            self._root = self.__Node(val)
            self._size += 1

    def inOrder(self):
        yield from self._inOrder(self._root)

    def addOrIncrementDomainNameNode(self, domainName):
        # searches BST for domainName
        node, found = self.search(domainName)
        if found: # using the public method
            # increment reference count
            node._count += 1
        else:  # if no match found insert new node
            self.insert(domainName)

    def printTree(self):
        for d, c in self.inOrder():
            print(d, c)


def populateTree(inFileName):
    tree = BST()
    infile = open(inFileName, "r")
    for l in infile:
        domain = l.split(":")[0]
        tree.addOrIncrementDomainNameNode(domain)
    return tree

if __name__ == "__main__":
    import argparse
    import sys
    import os.path

    parser = argparse.ArgumentParser(description="Linked list implementation of binary search tree")
    parser.add_argument("-i", "--inputFileName", type=str, help="The input file name")
    args = parser.parse_args()

    if not (os.path.isfile(args.inputFileName)):
        print("error,", args.inputFileName, "does not exist, exiting.", file=sys.stderr)
        exit(-1)

    tree = populateTree(args.inputFileName)
    tree.printTree()
