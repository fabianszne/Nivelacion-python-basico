# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:35:11 2018

@author: Fabian 
"""

from numpy import *

# en este codigo se implementa lo aprendido del video if else , de manera que se muestra un ejemplo extraido del video.
#este ejemplo analiza dos numeros y entrega cual es menor, igual o mayor.
#el ejemplo final es un codigo que pide al usuario un numero mayor a cero y permite saber si este es par o no.

h=3 #asignamos el valor 3 a la variable h 
f=6 #asignamos el valor 6 a la ariable f
if h<f: # si la variable h es menor que la variable f, se imprime h es menor que f
    print "h is less than f"
else: # imrpime que h no es menor que f si no se cumple lo del ciclo f
   if h == f:
       print " h is equal to f"
   else:
      print " f is greater than h "
      
      # codigo para ver si un numero es par "
numero = input( "ingrese un numero mayor a cero") # se le pide al usuario que ingrese un numero mayor a cero

if numero%2 == 0: # permite reconocer un numero para cuando al dividir por dos el resto es cero
    print " el numero es par " 
else: # sino, se imprime que el numero no es par
    print " el numero no es par"     