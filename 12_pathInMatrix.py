#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
class Solution():
    def findPathInMatrix(self,matrix,strList):
        if not matrix:
            return False
        rows=len(matrix)
        cols=len(matrix[0])
        visited=np.zeros((rows,cols),dtype=bool)
        pathLength=0
        for row in range(rows):
            for col in range(cols):
                if self.findPathInMatrixCore(matrix,rows,cols,row,col,strList,visited,pathLength):
                    return True
        return False


    def findPathInMatrixCore(self,matrix,rows,cols,row,col,strList,visited,pathLength):

        if pathLength==len(strList):
            return True
        hasPath=False
        if 0<=row<rows and 0<=col<cols and matrix[row][col]==strList[pathLength] and visited[row][col]==False:
            pathLength+=1
            visited[row][col]=True
            hasPath=self.findPathInMatrixCore(matrix,rows,cols,row-1,col,strList,visited,pathLength) or self.findPathInMatrixCore(matrix,rows,cols,row+1,col,strList,visited,pathLength) or self.findPathInMatrixCore(matrix,rows,cols,row,col-1,strList,visited,pathLength) or self.findPathInMatrixCore(matrix,rows,cols,row,col+1,strList,visited,pathLength)
        if not hasPath:
            pathLength-=1
            visited[row][col]=False
        return hasPath


if __name__=="__main__":
    sol=Solution()
    matrix=[['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
    strList="bfce"
    print(sol.findPathInMatrix(matrix,strList))


