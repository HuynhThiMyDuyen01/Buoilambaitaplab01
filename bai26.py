# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:49:40 2024

@author: MY DUYEN
"""
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print(a,b,c)
N=int(input("Nhập số nguyên N: "))
N=str(N)
sapxep=sorted(N)
print("".join(sapxep))
    
    
    
    
