#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution():
    def findMinInRotateArray(self,arrayList):
        if not arrayList:
            return None
        if arrayList[0]<arrayList[-1]:
            return arrayList[0]
        start=0
        end=len(arrayList)-1
        mid=(start+end)//2
        while (end-start)!=1:
            if arrayList[mid]>arrayList[start]:
                start=mid
            if arrayList[mid]<arrayList[end]:
                end=mid
            mid=(start+end)//2
        return arrayList[end]

if __name__=="__main__":
    sol=Solution()

    arrayList1=[1,2,3,4,5]
    print(sol.findMinInRotateArray(arrayList1))

    arrayList2=[2,3,4,5,1]
    print(sol.findMinInRotateArray(arrayList2))

    arrayList3=[3,4,5,1,2]
    print(sol.findMinInRotateArray(arrayList3))

    arrayList4=[4,5,1,2,3]
    print(sol.findMinInRotateArray(arrayList4))

    arrayList5=[5,1,2,3,4]
    print(sol.findMinInRotateArray(arrayList5))
