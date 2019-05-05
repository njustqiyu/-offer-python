#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy as np
class Solution():
    def fibonacciRecursion(self,n):
        if n<0:
            return None
        if n==0:
            return 0
        if n==1:
            return 1
        return self.fibonacciRecursion(n-1)+self.fibonacciRecursion(n-2)


    def fibFromBottom2Top(self,n):
        if n<0:
            return None
        result=np.zeros(n+1)
        result[1]=1
        for i in range(2,n+1):
            result[i]=result[i-1]+result[i-2]
        return int(result[n])

    def fib_3(self,n):
        if n<0:
            return None
        if n==0:
            return 0
        if n==1:
            return 1
        fib0=0
        fib1=1
        for i in range(2,n+1):
            fib=fib0+fib1
            fib0=fib1
            fib1=fib
        return fib

if __name__=="__main__":


    sol=Solution()

    print(sol.fibonacciRecursion(20))
    print(sol.fibFromBottom2Top(20))
    print(sol.fib_3(20))
