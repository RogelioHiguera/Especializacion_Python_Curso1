# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:46:07 2020

@author: RogelioTESI
"""

import numpy as np
def fibonacci(n):
    resultado = 0
    if n == 1 or n == 2:
        resultado =1
    elif n> 2:
        resultado = fibonacci(n-1) + fibonacci(n-2)
    return resultado

entrada = int(input('Mete el valor :'))
salida =0
salida = fibonacci(entrada)
print ('El resultado es :' , salida)