#! /usr/bin/python3

def fabonacci(num):
    a=1
    b=0
    for i in range(num):
        c=a+b
        b=a
        a=c
        print(c)
num = 10
fabonacci(num)