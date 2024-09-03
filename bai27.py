# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:10:28 2024

@author: MY DUYEN
"""
a=input("Nhập Hình: ")
if a=='v':
    canh=float(input("NHập cạnh hình vuông: "))
    if canh>0:
        print(f"Chu vi hình vuông: {canh*4}")
        print(f"Diện tích hình vuông: {canh**2}")
    else: 
        print("Không hợp lệ.")
elif a=='n':
    chieudai=float(input("Nhập chiều dài hình chữ nhật: "))
    chieurong=float(input("Nhập chiều rộng hình chữ nhật: "))
    if chieudai>0 and chieurong>0:
        print(f"Chu vi hình chữ nhật: {(chieudai+chieurong)*2}")
        print(f"Diện tích hình chữ nhật: {chieudai*chieurong}")
    else:
        print("Khong hợp lệ.")
elif a=='t':
    r=float(input("Nhập bán kính: "))
    if r>0:
        print(f"Chu vi hình tròn: {r*2*3.14}")
        print(f"Diện tích hình tròn: {(r**2)*3.14}")
else:
        print("Không hợp lệ.")