# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:10:05 2024

@author: MY DUYEN
"""
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
d=int(input("Nhập d: "))
if a<b and a<c and a<d:
    print(f"Số nhỏ nhất: {a}")
elif b<c and b<d:
    print(f"Số nhỏ nhất: {b}")
elif c<d:
    print(f"Số nhỏ nhất: {c}")
else:
    print(f"Số nhỏ nhất: {d}")