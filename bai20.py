# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:15:55 2024

@author: MY DUYEN
"""
a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
c=int(input("Nhập c: "))
if a>b and a>c:
    print(f"Số lớn nhất: {a}")
elif b>c:
    print(f"Số lớn nhất: {b}")
else:
    print(f"Số lớn nhất: {c}")
