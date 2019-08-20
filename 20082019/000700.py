# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 16:14:00 2018

@author: Fabian
"""

from numpy import *

# en el video se explican varias formas de definir una funcion, en una no se le dan parametros y en la otra, se le dan parametros.

def funcion1 (): # funcion que al llamarla imprime hola.
    print " hola " #imprimir hola.
    
    
funcion1() #llamando funcion.

def funcion2 (x): # funcion con parametro , que imprime  2*x.
    print 2*x 

p= funcion2(10) # se le asigna a una variable el valor de un nunero para la funcion2.

def funcion3 (x, y) : #funcion que recibe dos parametros , x e y y realiza la resta entre los valores que se le asignen.
    return x-y 
    
j= funcion3 (5,6) 
print j   

# minuto 7 corresponde a algunos ejercicios similares a los anteriormente mostrados.


# la siguiente funcion recibe el nombre, altura y peso de una persona.Permite conocer si una persona esta en su peso, bajo o sobre peso.
#esta funcion es una variante de la que se vee en el video.
name = raw_input("ingrese un nombre:")
height = float(input ("ingrese altura en metros(ejemplo : 1.80) :"))
weight = float(input (" igrese peso en kilogramos(ejemplo : 80):"))

def bmi_calculador(name, height, weight): #funcion que recibe tres parametros.
    bmi = weight / (height **2)
    print " bmi :", bmi
    if bmi < 25:
        return name + " is not overweight "
    else:
        return name + " is overweight"

resultado = bmi_calculador(name, height, weight)
print resultado

milla = float(input("ingrese un valor en millas :"))

# funcion que recibeel valor en millas y lo entrega en kilometros
def millas_a_kilometro( milla):
        kilometro = milla*1.6
        return    "El valor en kilometros es :" + str(kilometro)       
        
kilo = millas_a_kilometro(milla)
print kilo       
