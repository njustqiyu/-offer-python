#!/usr/bin/env python
# -*- coding:utf-8 -*-

class listNode():
    def __init__(self,data):
        self.value=data
        self.next=None

class Solution():
    def reverseList(self,pHead):
        if not pHead:
            return None
        pNode=pHead
        result=[]
        while pNode:
            result.append(pNode.value)
            pNode=pNode.next
        return result[::-1]

if __name__=="__main__":
    sol=Solution()
    a=listNode('a')
    b=listNode('b')
    c=listNode('c')
    d=listNode('d')
    a.next=b
    b.next=c
    c.next=d
    print(sol.reverseList(a))


