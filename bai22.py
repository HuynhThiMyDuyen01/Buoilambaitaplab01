# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:27:50 2024

@author: MY DUYEN
"""
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
if a==0:
    if b!=0:
        print("Phuong trinh vo nghiem.")
    else:
        print("Phuong trinh co vo so nghiem.")
else:
    x=-b/a
    print(f"Phuong trinh co nghiem x={x}")
