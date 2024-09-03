# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:04:57 2024

@author: MY DUYEN
"""
a=input("Nhập giờ phút giây: ")
gio=int(a.split('h')[0])
phut=int(a.split('h')[1].split('p')[0])
giay=int(a.split('h')[1].split('p')[1].split('s')[0])
print(gio*3600+phut*60+giay)