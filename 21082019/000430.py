# -*- coding: utf-8 -*-

"""
Created on Wed Aug 21 13:09:35 2019

@author: Fabian
"""

from numpy import *
 
#min 3 en adelante
lista = [4,5,6] 

lista.append(7) #agrega un el numero 8 al final de la lista
print lista 
print "la lista tiene" , len(lista) , "elementos" #imprime la lista mas su largo gracias al comando len().

#se pueden agregar string a la lista 

lista.append("hola")
print lista 

#ademas se pueden agregar listas dentro de nuestra lista.
lista.append([1,2,3])
print lista

#se puede eliminar un elemento de la lista con el comando pop(), que elimina el ultimo elemento de la lista.

lista.pop()
print lista

lista.pop()
print lista


print lista[1] #imprime el elemento que se encuetra en la posicion 1 de la lista.

#se puede reemplazar un numero de la lista de la siguiente manera.
lista[1] = 1
print lista

#a continuacion se muestra el ejercicio final del video , en donde cambio el orden de los elementos en la lista.
a= ["banana", "apple", "microsoft"]
print a
c = a[0]
a[0] = a[2]
a[2] = c
print a  
 

