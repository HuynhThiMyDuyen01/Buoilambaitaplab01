# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:20:33 2024

@author: MY DUYEN
"""
a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
if a>0 and b>0:
    laynguyen=a//b
    laydu=a%b
    print(f"Chia lấy nguyên: {laynguyen}")
    print(f"Chia lấy dư: {laydu}")
else:
    print("a, b không hợp lệ.")
