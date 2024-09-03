# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:56:16 2024

@author: MY DUYEN
"""
import math
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
s1=((a+b)/(math.pow(a, 1/3)+math.pow(b, 1/3)))-math.pow(a*b,1/3)
s2=(math.pow(a,1/3)-math.pow(b,1/3))**2
print(s1, s2)
s=s1/s2
print(s)
