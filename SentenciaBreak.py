# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:46:34 2020

@author: RogelioTESI
"""

def buscar_numero(numero,lista):
    """
    Busca numero en lista
    """
    indice = -1
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    return indice
numero1 = 7
lista = [1,3,4,5,6]
index = buscar_numero(numero1,lista)
for num in range(2,10):
    if num % 2 == 0:
        print("Encontre un número par: ", num)
        continue
    print("Encontre un número impar: ", num)
def a_funcion(x):
    resultado = 0
    if x>0 and x<5:
        resultado = x**2
    elif x>=5 and x<10:
        pass
    else: 
        resultado = (x**4)+1
    return resultado
x1=-1
result = a_funcion(x1)

s = 0
for n in range(1, 10):
   if n % 11 == 0:
         break;
   s += n
else:
    s += 10