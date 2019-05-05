#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution():
    def cutRope(self,n):
        if n<=1:
            return 0
        if n==2:
            return 1
        if n==3:
            return 2

        tempMax=0
        tempResults=[0]*(n+1)
        tempResults[0]=0
        tempResults[1]=1
        tempResults[2]=2
        tempResults[3]=3
        for i in range(4,n+1):
            for j in range(1,n//2+1):
                result=tempResults[j]*tempResults[i-j]
                if tempMax<result:
                    tempMax=result
            tempResults[i]=tempMax
        return tempResults[n]

if __name__=="__main__":
    sol=Solution()
    print(sol.cutRope(4))
    print(sol.cutRope(6))
    print(sol.cutRope(50))

