# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:49:03 2024

@author: MY DUYEN
"""
bankinh=float(input("Nhập bán kính hình tròn: "))
if bankinh>0:
    print(f"Chu vi hình tròn: {2*bankinh*3.14}")
    print(f"Diện tích hình tròn: {(bankinh**2)*3.14}")
else:
    print("Bán kính không hợp lệ.")