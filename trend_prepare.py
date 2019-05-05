#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution():
    #快排
    def quickSort(self,arrayList):
        if len(arrayList)<2:
            return arrayList
        else:
            middle=arrayList[0]
            less=[i for i in arrayList[1:] if i<=middle]
            greater=[j for j in arrayList[1:] if j>middle]
            return self.quickSort(less)+[middle]+self.quickSort(greater)

    #二路归并
    def mergeSort(self,arrayList):
        if len(arrayList)<=1:
            return arrayList

        middle=len(arrayList)//2
        left=arrayList[:middle]
        right=arrayList[middle:]

        left=self.mergeSort(left)
        right=self.mergeSort(right)

        result=[]
        while left and right:
            if left[0]<=right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        if left:
            result+=left
        if right:
            result+=right

        return result

    #冒泡排序
    def bubbleSort(self,arrayList):
        if len(arrayList)<=1:
            return arrayList
        n=len(arrayList)
        for i in range(n-1):
            for j in range(i,n-1):
                if arrayList[j]<=arrayList[j+1]:
                    arrayList[j],arrayList[j+1]=arrayList[j+1],arrayList[j]
        return arrayList[::-1]

    def noRepeatString(self,strList):
        if not strList:
            return None
        tempList=[]
        for str in strList:
            tempList.append(str)

        return (''.join(set(tempList)))



if __name__=="__main__":
    sol=Solution()
    # arrayList=[0,6,1,3,2,9,5,8,7,4]
    arrayList=[9,0,6,8,5,4,3,2,1,7]
    print(sol.quickSort(arrayList))
    print(sol.mergeSort(arrayList))
    print(sol.bubbleSort(arrayList))

    strList="assdddgghth"
    print(sol.noRepeatString(strList))
