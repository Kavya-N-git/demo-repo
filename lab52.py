#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 22:38:17 2021

@author: user
"""

#heirarchical inheitence
class student:
    def __init__(self):
        self.name=name
        self.usn=usn
        self.age=age
    def accept(self):
        self.name=input("enter student name: ")
        self.usn=input("enter student usn: ")
        self.age=int(input("enter your age: "))
        
class derived1(student):
    def __init__(self):
        self.sub1=0
        self.sub2=0
        self.sub3=0
        self.sub4=0
    def getmarks(self):
        self.sub1=int(input("enter computer basics marks: "))
        self.sub2=int(input("enter operating system marks: "))
        self.sub3=int(input("enter digital electronics marks: "))
        self.sub4=int(input("enter C programming marks: "))
        self.total=self.sub1+self.sub2+self.sub3+self.sub4
        self.per=(self.total/400)*100
        
    def display(self):
        print("-------------UG student details----------")
        print("name: ",self.name)
        print("usn: ",self.usn)
        print("age: ",self.age)
        print("computer basics marks: ",self.sub1)
        print("operating system marks: ",self.sub2)
        print("digital electronics marks: ",self.sub3)
        print("c programming marks ",self.sub4)
        print("maximum marks :400 ")
        print("marks scored: ",self.total)
        print("percentage scored: ",self.per)

class derived2(student):
    def __init__(self):
        self.sub1=0
        self.sub2=0
        self.sub3=0
        self.sub4=0
        self.sub5=0
    def getmarks(self):
        self.sub1=int(input("enter LSS marks: "))
        self.sub2=int(input("enter python marks: "))
        self.sub3=int(input("enter wap marks: "))
        self.sub4=int(input("enter cn marks: "))
        self.sub5=int(input("enter math marks: "))
        self.total=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
        self.per=(self.total/500)*100
        
    def display(self):
        print("-------------PG student details----------")
        print("name: ",self.name)
        print("usn: ",self.usn)
        print("age: ",self.age)
        print("LSS marks: ",self.sub1)
        print("python marks: ",self.sub2)
        print("wap marks: ",self.sub3)
        print("cn marks ",self.sub4)
        print("math marks: ",self.sub5)
        print("maximum marks :500 ")
        print("marks scored: ",self.total)
        print("percentage scored: ",self.per)

while True:
    print("1.UG STUDENTS\n2.PG students\n0.to exit")
    ch=int(input("enter your choice: "))
    if ch==1:
        n=int(input("enter no of students: "))
        for i in range(0,n):
            obj1=derived1()
            obj1.accept()
            obj1.getmarks()
            obj1.display()
    elif ch==2:
        n=int(input("enter no of students: "))
        for i in range(0,n):
            obj2=derived2()
            obj2.accept()
            obj2.getmarks()
            obj2.display()
    else:
        break