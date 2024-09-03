# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:24:19 2024

@author: MY DUYEN
"""
N=int(input("Nhập số dương N: "))
if 9<N<100:
    chuc=N//10
    donvi=N%10
    print(f"Tổng các chữ số của N: {chuc+donvi}")
