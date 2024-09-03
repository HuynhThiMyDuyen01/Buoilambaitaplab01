# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:36:41 2024

@author: MY DUYEN
"""
sinhnhat=input('Nhập Ngày Tháng Năm Sinh: ')
a=sinhnhat.split()
print(f"Ngày/Tháng/Năm: {a[0]+'/'+a[1]+'/'+a[2]}")
print(f"Ngày/Tháng/Năm: {a[0]+'/'+a[1]+'/'+a[2][-2:]}")
print(f"Năm/Tháng/Ngày: {a[2]+'/'+a[1]+'/'+a[0]}")
b=input('Nhập Ngày Tháng Năm Sinh (Ngày/Tháng/Năm): ')
c=b.split('/')
print(c[0]+" "+c[1]+" "+c[2])
print(c[0]+" "+c[1]+" "+c[2][-2:])
print(c[2]+" "+c[1]+" "+c[0])
