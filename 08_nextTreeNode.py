#!/usr/bin/env python
# -*- coding:utf-8 -*-

class listNode():
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.next=None

class Solution():
    def findNextTreeNode(self,pHead,pNode):
        if not pHead:
            return None
        if pNode.right:
            tempNode=pNode.right
            while tempNode.left:
                tempNode=tempNode.left
            return tempNode
        if not pNode.right:
            if pNode==pNode.next.left:
                return pNode.next
            if pNode==pNode.next.right:
                while pNode.next!=None and pNode!=pNode.next.left:
                    pNode=pNode.next
                return pNode.next

if __name__=="__main__":
    sol=Solution()
    a=listNode('a')
    b=listNode('b')
    c=listNode('c')
    d=listNode('d')
    e=listNode('e')
    f=listNode('f')
    g=listNode('g')
    h=listNode('h')
    i=listNode('i')
    a.left=b
    a.right=c
    b.left=d
    b.right=e
    b.next=a
    c.left=f
    c.right=g
    c.next=a
    d.next=b
    e.left=h
    e.right=i
    e.next=b
    f.next=c
    g.next=c
    h.next=e
    i.next=e
    print(sol.findNextTreeNode(a,a).value)
    print(sol.findNextTreeNode(a, b).value)
    print(sol.findNextTreeNode(a, c).value)
    print(sol.findNextTreeNode(a, e).value)

    print(sol.findNextTreeNode(a, d).value)
    print(sol.findNextTreeNode(a, f).value)
    print(sol.findNextTreeNode(a, h).value)


    print(sol.findNextTreeNode(a, g))
    print(sol.findNextTreeNode(a, i).value)



















