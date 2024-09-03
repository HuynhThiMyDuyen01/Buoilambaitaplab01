# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:52:02 2024

@author: MY DUYEN
"""
cannang=float(input("Nhập cân nặng: "))
chieucao=float(input("Nhập chiều cao: "))
if chieucao>0 and cannang>0:
    bmi=cannang/(chieucao**2)
    print(f"Số đo kiểm tra sức khỏe: {bmi}")
else:
    print("Chỉ số không hợp lệ.")