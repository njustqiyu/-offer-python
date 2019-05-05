#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution_1():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def appendTail(self,node):
        self.stack1.append(node)
        return self.stack1
    def deleteHead(self):
        if self.stack2:
            self.stack2.pop()
        elif not self.stack1:
            return None
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
        return self.stack2


class Solution_2():
    def __init__(self):
        self.Queue1=[]
        self.Queue2=[]

    def pushStack(self,node):
        self.Queue1.insert(0,node)
        return self.Queue1

    def popStack(self):
        if self.Queue2:
            return self.Queue2.pop()
        elif not self.Queue1:
            return None
        else:
            while len(self.Queue1)!=1:
                self.Queue2.insert(0,self.Queue1.pop())
            self.Queue1,self.Queue2=self.Queue2,self.Queue1
            return self.Queue2.pop()



if __name__=="__main__":

    # sol_1=Solution_1()
    # print(sol_1.appendTail(1))
    # print(sol_1.appendTail(2))
    # print(sol_1.appendTail(3))
    # print(sol_1.appendTail(4))
    # print(sol_1.deleteHead())
    # print(sol_1.deleteHead())
    # print(sol_1.deleteHead())
    # print(sol_1.deleteHead())
    # print(sol_1.deleteHead())


    sol_2=Solution_2()
    print(sol_2.pushStack(1))
    print(sol_2.pushStack(2))
    print(sol_2.pushStack(3))
    print(sol_2.pushStack(4))
    print(sol_2.popStack())
    print(sol_2.popStack())
    print(sol_2.popStack())
    print(sol_2.popStack())
    print(sol_2.popStack())




