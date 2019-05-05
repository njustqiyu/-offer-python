#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
class Solution():
    #10,斐波那契数列
    def fib(self,n):
        if n<0:
            return
        if n==0:
            return 0
        if n==1:
            return 1
        fib1=0
        fib2=1
        for i in range(2,n+1):
            fib=fib1+fib2
            fib1=fib2
            fib2=fib
        return fib

    #11，旋转数组最小的数
    def minNumInRotateArray(self,arrayList):
        if not arrayList:
            return None
        if arrayList[0]<arrayList[-1]:
            return arrayList[0]
        start=0
        end=len(arrayList)-1
        while (end-start!=1):
            if arrayList[start+1]>=arrayList[start]:
                start+=1
            if arrayList[end-1]<=arrayList[end]:
                end-=1
        return arrayList[end]

    #12,矩阵中的路径
    def pathInMatrix(self,matrix,strList):
        if not matrix or not strList:
            return None
        rows=len(matrix)
        cols=len(matrix[0])
        visited=np.zeros((rows,cols),dtype=bool)
        pathLength=0
        for row in range(rows):
            for col in range(cols):
                if self.pathInMatrixCore(matrix,row,col,pathLength,visited,strList):
                    return True
        return False

    def pathInMatrixCore(self,matrix,row,col,pathLength,visited,strList):
        rows=len(matrix)
        cols=len(matrix[0])
        if pathLength==len(strList):
            return True
        hasPath=False
        if 0<=row<rows and 0<=col<cols and visited[row][col]==False and matrix[row][col]==strList[pathLength]:
            visited[row][col]=True
            pathLength+=1
            hasPath=self.pathInMatrixCore(matrix,row-1,col,pathLength,visited,strList) or self.pathInMatrixCore(matrix,row+1,col,pathLength,visited,strList) or self.pathInMatrixCore(matrix,row,col-1,pathLength,visited,strList) or self.pathInMatrixCore(matrix,row,col+1,pathLength,visited,strList)
        if not hasPath:
            visited[row][col]=False
            pathLength-=1
        return hasPath


if __name__=="__main__":
    sol=Solution()

    #10,
    print(sol.fib(5))

    #11,
    arrayList=[3,4,5,6,7,1,2]
    print(sol.minNumInRotateArray(arrayList))

    #12,
    matrix=[['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
    print(sol.pathInMatrix(matrix,"bfco"))
