#!/usr/bin/env python
# -*- coding:utf-8 -*-

import heapq
class listNode():
    def __init__(self,data):
        self.value=data
        self.next=None


class Solution():

    #1,快排
    def quickSort(self,arrayList):
        if len(arrayList)<2:
            return arrayList
        else:
            middle=arrayList[0]
            less=[i for i in arrayList[1:] if i<=middle]
            greater=[j for j in arrayList[1:] if j>middle]
            return self.quickSort(less)+[middle]+self.quickSort(greater)

    #2,冒泡排
    def bubbleSort(self,arrayList):
        if not arrayList:
            return None
        n=len(arrayList)
        for i in range(n-1):
            for j in range(n-i-1):
                if arrayList[j]>arrayList[j+1]:
                    arrayList[j],arrayList[j+1]=arrayList[j+1],arrayList[j]
        return arrayList

    #3,旋转数组查找
    def findNumInRotateArray(self,arrayList):
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

    #4,反转链表
    def reverseList(self,pHead):
        if not pHead:
            return None
        pNode=pHead
        result=[]
        while pNode:
            result.append(pNode.value)
            pNode=pNode.next
        return result[::-1]

    #5,跳台阶
    def jumpFloor(self,n):
        if n<=0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        else:
            fib1=1
            fib2=2
            for i in range(3,n+1):
                fib=fib1+fib2
                fib1=fib2
                fib2=fib
            return fib

    #5-1,变态跳台阶
    def jumpFloorN(self,n):
        if n==1:
            return 1
        else:
            return self.jumpFloorN(n-1)*2

    #6,最小的k个数O(nlogn)
    def getLeastKNums_1(self,data,k):
        if not data or k<=0 or k>len(data):
            return None
        data.sort()
        return data[:k]

    def getLeastKNums_2(self,data,k):
        if not data or k<=0 or k>len(data):
            return None
        return heapq.nsmallest(k,data)

    #7,两个无序数组去重复
    def deleteRepeatNums(self,aList,bList):
        return sorted(list(set(aList+bList)))

    #8,扑克牌顺子
    def isContinuesNums(self,nums):
        if not nums or len(nums)!=5:
            return False
        nums_sort=sorted(nums)
        gap=0
        num_zeros=nums_sort.count(0)
        small=num_zeros
        big=small+1
        while big<len(nums):
            gap+=nums_sort[big]-nums_sort[small]-1
            small=big
            big+=1
        if gap<=num_zeros:
            return True
        else:
            return False

    #9,丑数
    def getUglyNum(self,n):
        if n<=0:
            return 0
        else:
            number=0
            uglyFound=0
            while uglyFound<n:
                number+=1
                if self.isUglyNum(number):
                    uglyFound+=1
            return number

    def isUglyNum(self,num):
        while num%2==0:
            num//=2
        while num%3==0:
            num//=3
        while num%5==0:
            num//=5
        return True if num==1 else False

    def getUglyNumber_2(self,index):
        if index<=0:
            return 0

        pUglyNumbers=[0]*index
        pUglyNumbers[0]=1
        nextUglyIndex=1

        id2,id3,id5=0,0,0
        while nextUglyIndex<index:
            minNum=min(pUglyNumbers[id2]*2,pUglyNumbers[id3]*3,pUglyNumbers[id5]*5)
            pUglyNumbers[nextUglyIndex]=minNum
            while pUglyNumbers[id2]*2<=pUglyNumbers[nextUglyIndex]:
                id2+=1
            while pUglyNumbers[id3]*3<=pUglyNumbers[nextUglyIndex]:
                id3+=1
            while pUglyNumbers[id5]*5<=pUglyNumbers[nextUglyIndex]:
                id5+=1
            nextUglyIndex+=1
        return pUglyNumbers[nextUglyIndex-1]

    #10,无序数组求中位数
    def getMidNUm(self,array):
        if not array:
            return None
        array_sort=sorted(array)
        n=len(array)
        if n%2==0:
            return (array_sort[n // 2-1] + array_sort[n // 2]) / 2
        else:
            return array_sort[n//2]


    #11,字符串中出现第k多的字符
    def getKAppearStr(self,strList,k):
        if not strList or k<=0:
            return ''
        result=[]
        tableSize=128
        hashTable=[0]*tableSize
        for hashkey in strList:
            hashTable[ord(hashkey)]+=1

        hashTable_sort=list(set(sorted(hashTable)))[::-1]
        # print(hashTable_sort)
        index=hashTable_sort[k-1]

        for hashkey in strList:
            if hashTable[ord(hashkey)]==index:
                if hashkey not in result:
                    result.append(hashkey)
        return result


    #12,判断是不是二叉排序树的后序结果
    def vertifySequenceOfBTS(self, sequence):
        if not sequence:
            return False
        root = sequence[-1]
        # 左子树的个数
        i = 0
        while sequence[i] < root:
            i += 1
        # 判断右子树的值是不是大于根节点
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        # 判断左子树是不是ＢＳＴ
        left = True
        if i > 0:
            left = self.vertifySequenceOfBTS(sequence[:i])
        # 判断右子树是不是ＢＳＴ
        right = True
        if i < len(sequence) - 1:
            right = self.vertifySequenceOfBTS(sequence[i:-1])
        return left and right


















if __name__=="__main__":
    sol=Solution()
    # arrayList=[6,4,9,0,8,8,1,5]
    # print(sol.quickSort(arrayList))
    # print(sol.bubbleSort(arrayList))
    #
    # arrayList1=[5,5,6,7,1,2,3,4,4]
    # print(sol.findNumInRotateArray(arrayList1))
    #
    # a=listNode(1)
    # b=listNode(2)
    # c=listNode(3)
    # a.next=b
    # b.next=c
    # print(sol.reverseList(a))
    #
    #
    # print(sol.jumpFloor(4))
    # print(sol.jumpFloorN(4))
    #
    # data=[0,9,77,2,8,12,4,5]
    # print(sol.getLeastKNums_1(data,3))
    # print(sol.getLeastKNums_2(data,3))
    #
    # aList=list(map(int,input().split()))
    # bList=list(map(int,input().split()))
    # print(sol.deleteRepeatNums(aList,bList))

    # print(sol.isContinuesNums([1,2,7,0,3]))
    # print(sol.isContinuesNums([1,5,4,2,3]))
    # print(sol.isContinuesNums([0,4,5,2,3]))
    # print(sol.isContinuesNums([2,5,6,7,8]))

    # print(sol.getUglyNum(5))
    # print(sol.getUglyNumber_2(5))


    # print(sol.getMidNUm([8,4,1,2,5,3,6,7]))

    print(sol.getKAppearStr("jjjjjaasdeeefgg",1))
    print(sol.getKAppearStr("jjjjjaasdeeefgg", 2))
    print(sol.getKAppearStr("jjjjjaasdeeefgg", 3))
    print(sol.getKAppearStr("jjjjjaasdeeefgg", 4))
    print(sol.getKAppearStr("jjjjjaasdeeefgg", 5))
