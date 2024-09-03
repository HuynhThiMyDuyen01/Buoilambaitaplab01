# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:31:25 2024

@author: MY DUYEN
"""
import math
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a==0:
    print("Phuong trinh la phuong trinh bac nhat.")
    if b==0:
        if c==0:
            print("Phuong trinh co vo so nghiem.")
        else:
            print("Phuong trinh vo nghiem.")
    else:
        x=-c/b
        print(f"Phuong trinh co nghiem x={x}")
else:
    delta=b**2-4*a*c
    if delta<0:
        print("Phuong trinh vo nghiem.")
    elif delta==0:
        x=-b/(2*a)
        print(f"Phuong trinh co nghiem kep x={x}")
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print(f"Phuong trinh co 2 nghiem phan biet x1={x1}\tx2={x2}")