# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:25:46 2024

@author: MY DUYEN
"""
gio1=int(input("Nhập giờ: "))
phut1=int(input("Nhập phút: "))
giay1=int(input("Nhập giây: "))
tg1=gio1*3600+phut1*60+giay1
gio2=int(input("Nhập giờ: "))
phut2=int(input("Nhập phút: "))
giay2=int(input("Nhập giây: "))
tg2=gio2*3600+phut2*60+giay2
cong=tg1+tg2
a=cong//3600
b=cong%3600//60
c=cong%3600%60
print(f'Tổng 2 giờ: {a} giờ {b} phút {c} giây')
if tg1>tg2:
    hieu=tg1-tg2
    a1=hieu//3600
    b1=hieu%3600//60
    c1=hieu%3600%60
    print(f'Hiệu 2 giờ: {a1} giờ {b1} phút {c1} giây')
else:
    hieu=tg2-tg1
    a1=hieu//3600
    b1=hieu%3600//60
    c1=hieu%3600%60
    print(f'Hiệu 2 giờ: {a1} giờ {b1} phút {c1} giây')