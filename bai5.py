# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:29:15 2024

@author: MY DUYEN
"""
thoigian=input("Nhập giờ phút giây theo định dạng (hh:mm:ss): ")
gio=int(thoigian[:2])
phut=int(thoigian[3:5])
giay=int(thoigian[6:])
quydoi=gio*3600+phut*60+giay
print(quydoi)
