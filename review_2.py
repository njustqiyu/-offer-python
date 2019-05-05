#!/usr/bin/env python
# -*- coding:utf-8 -*-

class binaryTreeNode():
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class nextNode():
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.next=None

class Solution():
    '''07,重建二叉树'''
    def reConstructTree(self,preOrder,inOrder):
        if not preOrder or not inOrder:
            return None
        pRoot=binaryTreeNode(preOrder.pop(0))
        rootIndex=inOrder.index(pRoot.value)
        pRoot.left=self.reConstructTree(preOrder,inOrder[:rootIndex])
        pRoot.right=self.reConstructTree(preOrder,inOrder[rootIndex+1:])
        return pRoot
    def prePrint(self,pRoot):
        if not pRoot:
            return None
        print(pRoot.value,end=' ')
        self.prePrint(pRoot.left)
        self.prePrint(pRoot.right)

    '''08,中序的下一个节点'''
    def nextNode(self,pNode):
        if not pNode:
            return None
        if pNode.right:
            tempNode=pNode.right
            while tempNode.left:
                tempNode=tempNode.left
            return tempNode
        if not pNode.right:
            if pNode==pNode.next.left:
                return pNode.next
            else:
                tempNode=pNode.next
                while tempNode.next!=None and tempNode!=tempNode.next.left:
                    tempNode=tempNode.next
                return tempNode.next

    '''09-1,两个栈代替队列'''
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.Queue1=[]
        self.Queue2=[]

    def appendTail(self,node):
        self.stack1.append(node)
        return self.stack1
    def deleteTail(self):
        if self.stack2:
            self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
        return self.stack2

    '''09-2,两个队代替栈'''
    def pushStack(self,node):
        self.Queue1.insert(0,node)
        return self.Queue1
    def popStack(self):
        if self.Queue2:
            return self.Queue2.pop()
        elif not self.Queue1:
            return None
        else:
            while len(self.Queue1)!=1:
                self.Queue2.insert(0,self.Queue1.pop())
            self.Queue1,self.Queue2=self.Queue2,self.Queue1
        return self.Queue2.pop()


if __name__=="__main__":
    sol=Solution()

    # #07,
    # preOrder=[1,2,4,7,3,5,6,8]
    # inOrder=[4,7,2,1,5,3,8,6]
    # pRoot=sol.reConstructTree(preOrder,inOrder)
    # sol.prePrint(pRoot)
    # print()
    #
    # #08,
    # a=nextNode('a')
    # b=nextNode('b')
    # c=nextNode('c')
    # d=nextNode('d')
    # e=nextNode('e')
    # f=nextNode('f')
    # g=nextNode('g')
    # h=nextNode('h')
    # i=nextNode('i')
    # a.left=b
    # a.right=c
    # b.left=d
    # b.right=e
    # b.next=a
    # c.left=f
    # c.right=g
    # c.next=a
    # d.next=b
    # e.left=h
    # e.right=i
    # e.next=b
    # f.next=c
    # g.next=c
    # h.next=e
    # i.next=e
    # print(sol.nextNode(a).value)
    # print(sol.nextNode(b).value)
    # print(sol.nextNode(c).value)
    # print(sol.nextNode(e).value)
    # print(sol.nextNode(d).value)
    # print(sol.nextNode(f).value)
    # print(sol.nextNode(h).value)
    # print(sol.nextNode(i).value)
    # print(sol.nextNode(g))

    # #09-1
    # print(sol.appendTail(1))
    # print(sol.appendTail(2))
    # print(sol.appendTail(3))
    # print(sol.appendTail(4))
    # print(sol.deleteTail())
    # print(sol.deleteTail())
    # print(sol.deleteTail())
    # print(sol.deleteTail())
    # print(sol.deleteTail())

    #09-2
    print(sol.pushStack(1))
    print(sol.pushStack(2))
    print(sol.pushStack(3))
    print(sol.pushStack(4))
    print(sol.popStack())
    print(sol.popStack())
    print(sol.popStack())
    print(sol.popStack())
    print(sol.popStack())
