# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:14:05 2024

@author: MY DUYEN
"""
import random
luachon=['Nguyên','Thực']
if random.choice(luachon)=='Nguyên':
    print(f'Số nguyên từ 0 đến 100: {random.randint(0,100)}')
    print(f'Số nguyên từ 50 đến 99: {random.randint(50,99)}')
    print(f'Số nguyên từ -39 đến 79: {random.randint(-39,79)}')
    print(f'Số nguyên từ -79 đến -39: {random.randint(-79,-39)}')
    
else:    
    print(f'Số thực từ 0 đến 100: {random.uniform(0,100)}')
    print(f'Số thực từ 50 đến 99: {random.uniform(50,99)}')
    print(f'Số thực từ -39 đến 79: {random.uniform(-39,79)}')
    print(f'Số thực từ -79 đến -39: {random.uniform(-79,-39)}')
    
