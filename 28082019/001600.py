# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:50:35 2019

@author: Fabian
"""
import numpy as np
from numpy import *

#se trabajara con arreglos. 
#se utilizaran debido que representan una mejor opcion para la optimizacion de un codigo, y resultan ser mas eficientes que las listas.
 
a = np.array([2,3,4])
print a

#se puede crear un arreglo con numeros entre el 1 y 12, que se espacien de a dos.
b=np.arange(1,12,2)
print " "
print b

aA = np.linspace(1,12,6) #se crea arrgeglo con numeros entre 1 y 12, con un numero total de 6 elementos.
print " "
print aA

#podemos transformar un arreglo a dos dimensiones.A dos columnas y tres filas.
aaaa = aA.reshape(3,2)
print aaaa

print " "
print aaaa.size #entrega el tamaño del arreglo. Cantidad de elementos
print " "
print aaaa.shape #muestra las dimensiones
print" "
print aaaa.dtype # muestra que es un arreglo del tipo numerico float
print aaaa.itemsize #muestra el espacio en bits que ocupa en la memoria, ene este caso 8 bytes
#se puede crear un agreglo multidimensionl, como el siguiente que es bidimensional.

xl = np.array([(1,2,4,5),(6,8,9,)]) 
 
print " "
print xl
print " "
print aaaa < 4 #muestra como true los elmentos que cumplen la condicion y false los que no la cumplen.
print " "
print aaaa > 5
print" "
print aaaa*3  #imprime el arreglo pero con todos los numeros multiplicados por 3.


#se pueden crear arreglos de puros ceros.
l = np.zeros((3,4)) #posee 4 columnas y 3 filas.
print"  "
print l
print" "

lL = np.random.random ((2,3)) 
print lL
np.set_printoptions(precision =2, suppress = True) #permite elminiar los decimales segun se necesite, para dar mayor precision en el valor numerico.
print" "

Asa = np.random.randint(0,10,5) #arreglo del 0 al 10 incluidos, de 5 elementos.
print Asa 
print" "
print Asa.sum() # muestra la suma de los elementos del arreglo.
print " "
print Asa.max() #entrega el mayor de los elementos
print""
print Asa.min() #entrega el menor de los elementos
print " "
print Asa.var() #varianza
print" "
print Asa.std() #desviacion estandar.
print""

lsh = np.random.randint(1,10,6)
lls= lsh.reshape(3,2) #arreglo de 3 filas y 2 columnas.
print lls
print ""
print lls.sum(axis=1) #suma los elementos  de una fila 
print lls.sum(axis=0) #suma los elementos de una columna

#podemos importar un archivo de texto o un archivo cvs en una sola linea de codigo.
#data= np.loadtxt( "data.txt", dtype=np.uint8, delimiter= ",", skiprows=1)


cj = np.arange(10)
print " "
np.random.shuffle(cj) #ordena el arreglo de una forma aleatorea
print cj
print ""
print np.random.choice(cj) #imprime al azar un elemnto del arreglo

