# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 00:26:52 2020

@author: RogelioTESI
"""

def es_primo(Numero):
    resultado = True
    rep = 0
    for divisor in range(2,Numero):
        if (Numero % divisor)==0:
            resultado = False
            break
    rep = rep+(divisor-1)
    return resultado,rep
x,rep = es_primo(13)
    