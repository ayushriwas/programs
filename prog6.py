#! /usr/bin/python3
#find duplicate characters in string.

def dub(str):
    a=[]
    for i in range(len(str)):
        print(str[i])
        if i < len(str) and str[i]==str[i+1]:
            a.append(str[i])
    return a

str = "aayuush"
res = dub(str)
print(res)