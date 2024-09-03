# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:01:24 2024

@author: MY DUYEN
"""
bienxe=int(input("Nhập biển số xe của bạn gồm 4 chữ số: "))
a=bienxe//1000
b=bienxe%1000//100
c=bienxe%1000%100//10
d=bienxe%1000%100%10
sonut=(a+b+c+d)%10
print(f"Số nút: {sonut}")


