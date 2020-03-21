# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:46:48 2020

@author: RogelioTESI
"""
import numpy as np 
import matplotlib.pyplot as plt
Em=10
Ec=20
fm=5e3
fc=100e3
Tm=1/fm
t=np.linspace(0,2*Tm,num=2000)
Vm=Em*np.sin(2*np.pi*fm*t)
Vc=Ec*np.sin(2*np.pi*fc*t)
Vmod=(Ec+Em*np.sin(2*np.pi*fm*t))*np.sin(2*np.pi*fc*t)
fig,axes=plt.subplots()
axes.plot(t*1000,Vm)
axes.plot(t*1000,Vc)
axes.set_xlabel('Time(ms)')
axes.set_ylabel('Amplitud(V)')
plt.grid(True)
fig1,axes1=plt.subplots()
axes1.plot(t*1000,Vmod)
axes1.set_xlabel('Time(ms)')
axes1.set_ylabel('Amplitud(V)')
plt.grid(True)