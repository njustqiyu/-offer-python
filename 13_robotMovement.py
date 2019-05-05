#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np

class Solution():
    def robotMovement(self,m,n,k):
        if not m and not n:
            return None

        if m<=0 or n<=0 or k<=0:
            return 0
        visited=np.zeros((m,n),dtype=bool)
        count=self.robotMovementCore(m,n,k,0,0,visited)
        return count


    def robotMovementCore(self,rows,cols,k,row,col,visited):
        count=0
        if self.checkValid(rows,cols,k,row,col,visited):
            visited[row][col]=True
            count=1+self.robotMovementCore(rows,cols,k,row-1,col,visited)+self.robotMovementCore(rows,cols,k,row+1,col,visited)+self.robotMovementCore(rows,cols,k,row,col-1,visited)+self.robotMovementCore(rows,cols,k,row,col+1,visited)
        return count

    def checkValid(self,rows,cols,k,row,col,visited):
        if  0<=row<rows and 0<=col<cols  and self.getDigitSum(row)+self.getDigitSum(col)<=k and visited[row][col]==False:
            return True
        else:
            return False

    def getDigitSum(self,num):
        s=0
        while num:
            s+=num%10
            num=num//10
        return s

if __name__=="__main__":
    sol=Solution()
    print(sol.robotMovement(15,1,100))



