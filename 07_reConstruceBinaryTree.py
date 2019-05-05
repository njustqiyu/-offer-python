#!/usr/bin/env python
# -*- coding:utf-8 -*-

class binaryTreeNode():
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class Solution():
    def reConstructTree(self,preOrder,inOrder):
        if not preOrder or not inOrder:
            return None
        pRoot=binaryTreeNode(preOrder.pop(0))
        rootIndex=inOrder.index(pRoot.value)
        pRoot.left=self.reConstructTree(preOrder,inOrder[0:rootIndex])
        pRoot.right=self.reConstructTree(preOrder,inOrder[rootIndex+1:])
        return pRoot

    def prePrint(self,pRoot):
        if not pRoot:
            return None
        print(pRoot.value,end=' ')
        self.prePrint(pRoot.left)
        self.prePrint(pRoot.right)


if __name__=="__main__":

    sol=Solution()
    preOrder=[1,2,4,7,3,5,6,8]
    inOrder=[4,7,2,1,5,3,8,6]
    pRoot=sol.reConstructTree(preOrder,inOrder)
    sol.prePrint(pRoot)

        



