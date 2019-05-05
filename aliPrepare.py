#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import  Iterator

class MyList(list):
    def __hash__(self):
        return hash(self[0])

class Solution():
    def fib(self,max):
        n,a,b=0,0,1
        while n<max:
            yield b
            a,b=b,a+b
            n=n+1
        return 'done'


if __name__=="__main__":
    #1,list\tuple
    # a_tuple=(2,)
    # mixed_tuple=(1,2,['a','b'])
    # print(a_tuple)
    # print(mixed_tuple)
    # mixed_tuple[2][0]='c'
    # print(mixed_tuple[2])

    # #2,dict的key
    # s=MyList([1,8])
    # dict={'a':1,s:4,'c':3}
    # print(dict)

    #3,生成器，迭代器
    #列表生成式
    lis=[x*x for x in range(10)]
    print(lis)
    #生成器
    generator_ex=(x*x for x in range(10))
    # print(next(generator_ex))
    for i in generator_ex:
        print(i,end=' ')
    print()

    sol=Solution()
    # a=sol.fib(10)
    # print(sol.fib(10))
    # print(a.__next__())
    for i in sol.fib(6):
        print(i,end=' ')
    print()

    print(isinstance((x for x in range(10)),Iterator))
    print(isinstance([],Iterator))


