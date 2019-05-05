#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution():
    def reSort(self,arrayA,arrayB):

        if not arrayA:
            return arrayB
        if not arrayB:
            return  arrayA
        endA=len(arrayA)-1
        endB=len(arrayB)-1

        arrayA=arrayA+arrayB
        end=len(arrayA)-1


        while endB>=0:
            if arrayA[endA]>arrayB[endB]:
                arrayA[end]=arrayA[endA]
                endA-=1
                end-=1
            else:
                arrayA[end] = arrayB[endB]
                endB -= 1
                end -= 1
        return arrayA

if __name__=="__main__":

    # str="We are happy."
    # print(str.replace(' ','%20'))

    sol=Solution()
    arrayA=[1,3,5,7,9]
    arrayB=[3,4,6,10]
    print(sol.reSort(arrayA,arrayB))
