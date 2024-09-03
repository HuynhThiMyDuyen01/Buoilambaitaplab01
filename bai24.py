# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:38:00 2024

@author: MY DUYEN
"""
gio=int(input("Nhập giờ: "))
phut=int(input("Nhập phút: "))
giay=int(input("Nhập giây: "))
if 0<=gio<24:
    if 0<phut<=59:
        if 0<giay<=59:
            print("Giờ, phút, giây hợp lệ.")
        else:
            print("Không hợp lệ.")
    else:
        print("Không hợp lệ.")
else: 
    print("Không hợp lệ.")