#! /usr/bin/python3

# factorial using loop 
def loop(a):
    for i in range(1,a):
        a=a*i
        
    print(a)

def recursion(a):
    if a==0 or a==1:
        return 1
    return a * recursion(a-1)

a=int(input("Enter a no: "))
loop(a)
res = recursion(a)
print(res)