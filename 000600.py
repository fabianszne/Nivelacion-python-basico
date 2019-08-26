# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:37:01 2019

@author: Fabian
"""
from numpy import *

# creamos un diccionario vacio y luego se agregan elementos en el. 
d = {}

d ["Fabi"] = 25 # se agrega el string fabi y su valor asociado, que en este caso es 25.
d ["jesus"] = 2000
d["juan"] = 50
print d
print d["Fabi"] #imprime el valor asociado al string Fabi.


# el valor asociado a un elemento del diccionario puede ser reemplazado por uno nuevo, de la siguiente manera.
d["juan"] = 100
print d["juan"]
print d

#el valor asociado al keys , puede cambiar pero el keys puede ser solo de cierto tipo y eisten diferentes tipos que se pueden usar para hacer eso.
#los keys mas comunes son strings y numeros.
 
d[10]=55
print d
print d[10]

#se puede iterar sobre los pares key-value de un diccionario.
for key,value in d.items():
     print "key :"
     print key
     print "valor:"
     print value
     print " "
     