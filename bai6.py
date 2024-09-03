# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:46:06 2024

@author: MY DUYEN
"""
namsinh=int(input("Nhập năm sinh: "))
if 0<namsinh<=2022:
    print(f"Ban sinh nam {namsinh} vay ban {2022-namsinh} tuoi.")
else:
    print("Năm sinh không hợp lệ.")
