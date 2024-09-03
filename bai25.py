# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:45:25 2024

@author: MY DUYEN
"""
a=input("Nhập 1 chữ cái: ")
if len(a)>1:
    print("Không hợp lệ.")
else:
    if a.islower():
        print(a.upper())
    else:
        print(a.lower())
