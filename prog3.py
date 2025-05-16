#! /usr/bin/python3

#prime 
def prime(a):
    for i in range(2,a):
        if a%i==0:
            print("False",i)
            break
        else:
            print("True")
            
a=5
prime(a)