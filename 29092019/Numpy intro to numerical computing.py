# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:07:16 2019

@author: Fabian
"""
import numpy as np

a = [1,2,3,4]
b= [10, 11, 12, 13]

print a + b 
output = []
for item1, item2 in zip(a,b): 
#este tipo de codigo resulta un poco lento y ocupa espacion en la memoria.
#este ciclo suma los elementos de a y b, pero suma los que se encuntran en la misma posicion y los agrega en una lista vacia
    output.append(item1 + item2) 
print ""
print output

g = list(range(1000000))
#%timeit sum (g) # se puede ve cuanto tadra el ordenador en realizar la suma en el siguiente codigo. Se nota que al hacerlo, esta mas rapida de lo que un hombre lo haria per es muy lenta en comparacion a lo que un computador haria.

g_array = np.array(g) #ponemos la lista en un arreglo

#%timeit np.sum(g_array) #al usar este comando se puede notar que existe un beneficio de usar arreglos. 1000 lops en vez de 100.

a = np.array ([1,2,3,4])
b = np.array([10,11,12,13])
print " " 
print a
print""
print b
print ""
print a+b #numpy hace lo mismo que el ciclo for anterior pero de manera mas rapida y eficiente

print " "
print a*b
print""
print a/b
print""
print a**b

#chequea el tipo 
print type(a)
#chequea el tipo numerico 
print a.dtype
#chequea el numero de dimensiones
print a.ndim
#bytes por elmento
print a.itemsize
#bytes de la memoria usados
print a.nbytes
#la forma o largo, a lo largo de cada dimension, mostrado como tupla
print a.shape

fF=(5,6)
print type(fF) #mmuestra que es una tupla , se identifica que es tupla porque tiene coma (,)

#algunas operaciones matematicas 
print a * 100 #se puede operar un arreglo. en este caso se multplican por 100 todos los elementos
print np.sin(a)
print np.exp(a)

a[0]= 10 #se puede reemplazar el numeero deseado en la posicion [] del arreglo
print a


a= np.array([1,2,3,4])

a= np.array([1,2,3,4.0])
print ""
print a.dtype #muestra que es float

a = np.array([1,2,3,4.0+1j])
print a.dtype #muestra que es complejo
#puedo forzar a que el array sea de cierto tipo
a = np.array([1,2,3,4.0] , dtype = 'int32')
print " "
print a.dtype

c = np.array([[10,11,12],[20,21,22]]) #arreglo bidimensional
print c

print c.ndim
print c.shape
print c.size

print c[0,1] #muestra el elemento 1 de la lista que ocupa la posicion 0 
print c[0] # imprime la lista en la posicion 0

#            -5 -4  -3 -2 -1
#             0  1   2  3  4
a = np.array([10,11,12,13,14])
print ""
print a[1:3] #muestra el numero que esta la posicion 1 hasta la 3 sin incluir el 3

#se puede usar numeracion negativa para imprimir lo mismo que a[1:3]
print a[1:-2]
print a[-4:3]

#se puede mostrar cierta cantidad de numeros del arreglo al definir solo la cota superior
print a[:-1]

print "   "
#ejercicio
#imprmir del arreglo ciertos numeros.
a = np.arange(25).reshape(5,5)# crea arreglo con 25 numeros desde el cero hasta el 25 sin el 25. y ademas lo deja de 5x5.

print a
red =a[:,1::2]
print red #imprime columna 1  y 3 contando desde  0
print ""

yellow = a[4:, :] # imprime ultima fila del arreglo
print yellow

celeste1 = a[1:2,0:1]
celeste2 = a[1:2,2:3]
celeste3 = a[3:4,0:1]
celeste4 = a[3:4,2:3]
print celeste1
print celeste2
print celeste3
print celeste4

blue = a[1::2, :3:2]
# imprime el 5,7 15 y 17 juntos en un arreglo , a partir edel arreglo a
print blue
print ""

a = np.arange(0, 80, 10) 
# 0 10 20 30 40 50 60 70 
indices = [1,2,-3]
y =a[indices]
print y # se imprimen los numeros que se encuentran en la posicion numerica del indice.
print ""
aA = np.array([3,5,-6,-7,9,-2])
aA[aA<0] = 100 #reemplazo los negativos por 100
print aA 

# ~ (not), & (and) 
#^ (xor)

print ""

Aaa = np.arange(25).reshape(5,5)
print ""
print Aaa
print Aaa%3 #se extraen los numeros divisibles por 3, los ceros son los divisibles por 3
print  ""
print Aaa[Aaa%3 == 0] # muestra cuales son divisibles por 3

#output = np.full_like(Aaa, np.nan, dtype = 'float')
#mask = Aaa%3 ==0
#output[mask] = Aaa[mask]


al = np.array([1,2,3])
print np.sum(al)#suma los elementos del arreglo

ali =  np.array([[1,2,3],[4,5,6]])
print np.sum(ali)# suma igual que antes

print ali.sum(axis = 0) #suma en el eje o , es decir hacia abajo
print ali.sum(axis = -1) #suma en el eje -1 , es decir hacia la derecha

#se pueden encontrar minimos y maximos, argmin y argmax

print al.min(axis = 0) 
print np.min(al, axis = 0)

print al.max(axis=0)
print np.max(al, axis =0)# como funcion







