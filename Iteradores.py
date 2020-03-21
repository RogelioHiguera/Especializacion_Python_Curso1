# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:42:38 2020

@author: RogelioTESI
"""
class Reversa:
    """Iterador para recorrer una secuencia de atrás para adelante."""
    def __init__(self,datos):
        self.datos = datos
        self.indice = len(datos)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice == 0:
            raise StopIteration()
        self.indice = self.indice - 1
        return self.datos[self.indice]
for elemento in Reversa([1,2,3,4]):
    print(elemento)
lista = [1,2,3]
it = iter(lista)
print(next(it))
print(next(it))
print(next(it))
print(next(it))