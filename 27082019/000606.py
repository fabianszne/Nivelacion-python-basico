# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:07:14 2019

@author: Fabian
"""


import numpy as np

#en este codigo se trabaja con arreglos.
#un arreglo corresponde a una estructura de datos muy similar a una lista pero que solamente trabaja con numeros como elementos, ya sea int o float.
#a continuacion se muestra un arreglo de tres ceros en float
a = np.zeros(3)
print a
#es posible cambiar la forma de un arreglo
p = np.zeros(10)
print p
p.shape = (10,1) #deja una columna de 10 ceros
print p


#se pueden crear arreeglos con unos
m = np.ones(10)
print m
print " "
#se puede crear un arreglo con el comando linspace
t = np.linspace(2,10,5) # va del 2 al 10, con 5 elementos
print t
print " "

#se puede crear un arreglo a partir de una lista
a_list = [1,2,3,4,5,6]
x = np.array([a_list])
print x
print " "

b_list = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7]] 
f = np.array([b_list])
print f
print " "

# se puede crear un arreglo con numeros al azar entre 0 y 14 , de un largo definido como se vee en el siguiente ejemplo.
np.random.seed(0)
xl = np.random.randint(14, size = 6)
print xl

# en  video se muestra un ejemplo de uso de arreglos con un foto, que es usada como elemetno y que posee ciertas dimensiones, que se traducen en un arreglo.
#el codigo solo se mostrara como ejemplo

#from skimage import io
#photo = io.imread ('york_minster.jpg)
#import matplotlib.pylot as plt
#plt.imshow (photo)
 
#se puede girar la imagenen 180 grados
 #plt.imshow(photo[::-1]
 
#se puede crear un efecto espejo al invertir las columnas de la imagen.
  #plt.imshow(photo[:, ::-1])
 
#es posible tomar solo tomar una seccion de la imagen.
 #plt.imshow(photo[50:150, 150:280]) 


#se puede analizar lo que esta dentro del arrgelo, por ejemplo ver si los numero que posee, son menores que 3 o mayores que 3 

j = np.array([1,2,3,4,5,6])
print j < 3
print j > 3

print j[j>3] #imprime solo los numeros mayores a 3.
print " "
#es posible sumar dos arreglos

a_array = np.array([1,2,3,4,5,6,7])
b_array = np.array([8,9,10,11,12,13,14])

print a_array + b_array 
print " "
print a_array + 50 #suma 50  todos los elementos del arreglo.

print" "
print a_array *10 #multiplica por 10 a todos los elementos del arreglo.