#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:24:17 2020

@author: pamela
"""

#Primer modelo
#Se consideran únicamente las locaciones a y b

#Definir la matriz de probabilidad para a y b (ejemplo de la forma matricial)

import numpy as np 
M = np.matrix([[0.8,0.4],[0.2,0.6]])
print(M)

#conocer la probabilidad de que se encuentre en otra ubicación en el futuro, 
#durante los siguientes n ensayos, al saber con certidumbre que el agente se
#encuentra en la ubicación b

#se define estado inicial b

P = np.matrix([[0], [1]])

#definición de la distribución de probabilidad

def dist_prob(T,x_0,n):
    x_n = np.matmul(np.linalg.matrix_power(M,n),x_0)
    print('P(t+'+str(n)+')=\n'+str(x_n))
    
P_7 = dist_prob(M,P,6) #llamar a los ensayos que se requieran, en este caso hasta 6

#en P_7 conocemos únicamente este valor, pero si se desan conocer los valores de 
#P_1 a P_7, realizar el siguiente ciclo for 

for i in range(7):
    dist_prob(M,P,i)
    
#en el ensayo anterior en 6, es posible reconocer que se llega a una convergencia, pero 
#cómo saber cuándo llegar a esta convergencia, sin la necesidad de calcular lo anterior
    
#se calculan eigenvectores

e,s = np.linalg.eig(M)
print(e)
print(s)

#Identificar la columna correspondiente al eigenvalor 1
#normalizarlo

e_v = s[:,0] / sum(s[:,0])
print(e_v)

#notar que el resultado es el mismo que en P(t+6), es decir, conocemos la convergencia
#sin necesidad de caluclar todos los valores anteriores

#%%

#Segundo modelo
#Se consideran  las locaciones a, b y c

#Definir la matriz de probabilidad para a y b (ejemplo de la forma matricial)

import numpy as np 

M = np.matrix([[0.6,0.1,0.2], [0.3,0.7,0.3], [0.1,0.2,0.5]])
print(M)

#conocer la probabilidad de que se encuentre en otra ubicación en el futuro, 
#durante los siguientes n ensayos, al saber con certidumbre que el agente se
#encuentra en la ubicación a

#se define estado inicial a

P = np.matrix([[1], [0], [0]])

#definición de la distribución de probabilidad

def dist_prob(T,x_0,n):
    x_n = np.matmul(np.linalg.matrix_power(M,n),x_0)
    print('P(t+'+str(n)+')=\n'+str(x_n))
    
P_7 = dist_prob(M,P,6) #llamar a los ensayos que se requieran, en este caso hasta 6

#en P_7 conocemos únicamente este valor, pero si se desan conocer los valores de 
#P_1 a P_7, realizar el siguiente ciclo for 

for i in range(6):
    dist_prob(M,P,i)
    
#en el ensayo anterior en 6, es posible reconocer que se llega a una convergencia, pero 
#cómo saber cuándo llegar a esta convergencia, sin la necesidad de calcular lo anterior
    
#se calculan eigenvectores

e,s = np.linalg.eig(M)
print(e)
print(s)

#Identificar la columna correspondiente al eigenvalor 1

e_v = s[:,0] / sum(s[:,0])
print(e_v)

#%%

#Tercer modelo
#Se consideran  las locaciones a, b, c y d

#primero se define la matriz de probabilidad

#Definir la matriz de probabilidad para a y b (ejemplo de la forma matricial)

import numpy as np 

M = np.matrix([[0.4,0.2,0.1,0.3], [0.3,0.5,0.3,0.1], [0.2,0.2,0.4,0.2], [0.1,0.1,0.2,0.4]])
print(M)

#definir el estado inicial
#agente se encuentra en el estado d

P = np.matrix([[0], [0], [0], [1]])

#definición de la distribución de probabilidad

def dist_prob(T,x_0,n):
    x_n = np.matmul(np.linalg.matrix_power(M,n),x_0)
    print('P(t+'+str(n)+')=\n'+str(x_n))
    
P_7 = dist_prob(M,P,6) #llamar a los ensayos que se requieran, en este caso hasta 6

#en P_7 conocemos únicamente este valor, pero si se desan conocer los valores de 
#P_1 a P_7, realizar el siguiente ciclo for 

for i in range(6):
    dist_prob(M,P,i)
    
#en el ensayo anterior en 6, es posible reconocer que se llega a una convergencia, pero 
#cómo saber cuándo llegar a esta convergencia, sin la necesidad de calcular lo anterior
    
#se calculan eigenvectores
e,s = np.linalg.eig(M)
print(e)
print(s)

#Identificar la columna correspondiente al eigenvalor 1

e_v = s[:,0] / sum(s[:,0])
print(e_v)