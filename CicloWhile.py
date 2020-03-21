# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 01:46:30 2020

@author: RogelioTESI
"""
def suma_n (n):
    result = 0
    x = n
    while x>0:
        result = result+x
        x = x-1
    return result
Rel = suma_n(5)
n = 1000
def primos (n):
    y = 0
    x = 0
    for i in range (1,n):
        if i%2 == 0:
            if y<50:
                x = i+x
                y = y+1
                print(i)
    return x
x = primos(n)
print(x)


