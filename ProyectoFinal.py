# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:31:25 2020

@author: RogelioTESI
"""
import random 
Dado1 = random.choice([1,2,3,4,5,6])
print("El número del Dado 1 es: ", Dado1)
Dado2 = random.choice([1,2,3,4,5,6])
print("El número del Dado 2 es: ", Dado2)
Suma = Dado1 + Dado2
print("La suma de los números de ambos Dados es: ", Suma)
print("¿Desea volver a tirar los dados?")
Valor = input("Escribir Si/No: ")
while Valor == "Si":
    Dado1 = random.choice([1,2,3,4,5,6])
    print("El número del Dado 1 es: ", Dado1)
    Dado2 = random.choice([1,2,3,4,5,6])
    print("El número del Dado 2 es: ", Dado2)
    Suma = Dado1 + Dado2
    print("La suma de los números de ambos Dados es: ", Suma)
    print("¿Desea volver a tirar los dados?")
    Valor = input("Escribir Si/No: ")
else:
    print("Hoy no es tu día de suerte")
     