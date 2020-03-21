# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:39:19 2020

@author: RogelioTESI
"""
for i in range(10):
    print(i)

for i in 'Hola Mundo' :
    print(i)

def contador(n):
    c=0
    for i in range(n):
        c+=1
    return c
a = contador(10)

def sumatoria (numeros):
    acum = 0
    for n in numeros:
        acum += n
    return acum
resultado = sumatoria([1,2,3,4,5])