#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''复习4/19的内容'''
import numpy as np

class listNode():
    def __init__(self,data):
        self.value=data
        self.next=None


class Solution():
    '''03,哈希表'''
    def findRepeatNum(self,arrayList):
        if not arrayList:
            return None
        length=len(arrayList)
        hashTable=np.zeros(length)
        for num in arrayList:
            hashTable[num]+=1
        result=[]
        for i in range(length):
            if hashTable[i]>=2:
                result.append(i)
        return result

    '''04,右上角比较'''
    def findNumInMatrix(self,matrix,key):
        if not matrix:
            return False
        rows=len(matrix)
        cols=len(matrix[0])
        if key<matrix[0][0] or key>matrix[rows-1][cols-1]:
            return False
        row=0
        col=cols-1
        while row<rows and col>=0:
            if key<matrix[row][col]:
                col-=1
            if key>matrix[row][col]:
                row+=1
            if key==matrix[row][col]:
                return True
        return False

    '''05,替换空格'''
    def replaceSpace(self,strList):
        if not strList:
            return None
        else:
            return strList.replace(' ','%20')

    '''05-1.合并数组，两个指针'''
    def mergeArrays(self,arrayA,arrayB):
        if not arrayA:
            return arrayB
        if not arrayB:
            return arrayA
        endA=len(arrayA)-1
        endB=len(arrayB)-1
        arrayA=arrayA+arrayB
        end=len(arrayA)-1
        while endB>=0:
            if arrayA[endA]>=arrayB[endB]:
                arrayA[end]=arrayA[endA]
                endA-=1
                end-=1
            else:
                arrayA[end]=arrayB[endB]
                endB-=1
                end-=1
        return arrayA

    '''06,反转链表'''
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
    arrayList=[2,3,1,0,2,5,3]
    print(sol.findRepeatNum(arrayList))

    matrix=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    print(sol.findNumInMatrix(matrix,7))

    strList="We are happy."
    print(sol.replaceSpace(strList))

    arrayA=[1,3,5,7,9]
    arrayB=[3,4,6,10]
    print(sol.mergeArrays(arrayA,arrayB))

    a=listNode(1)
    b=listNode(2)
    c=listNode(3)
    d=listNode(4)
    a.next=b
    b.next=c
    c.next=d
    print(sol.reverseList(a))
