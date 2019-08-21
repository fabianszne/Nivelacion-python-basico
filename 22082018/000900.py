# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:00:45 2019

@author: Fabian
"""

lista = ["banana","apple","microsoft"]
for element in lista: #ciclo que recorre la lista e imprime los elementos de manera ordenada.
    print element

lista2 = [4,5,6] # se crea una lista con numeros
total = 0
for element in lista2: #en este ciclo se recorre la lista y se suman todos los elementos.
    total = total + element #al valor de total que inicialmente es cero, le suma el primer valor de la lista, luego el segundo y finalmente el tercero.

    
print total
    

listita = range(1,5) # range()crea una lista desde el 1 hasta el 4.
print listita

#se puede recorrer un range( ) sin necesidad de hacer la lista previamente
#a continuacion se muestra un codigo realizado a partir de lo aprendido en el video.
total2 = 0
for i in range(1,10): #este ciclo le suma uno a total2 siempre y cuando exista un numero divisible por dos.
    if i%2 == 0:
        total2 +=1
        print str(i) + " es divisible por dos por lo tanto se suma 1"
    else:
        print str(i) + " no es divisible por dos por ende no se suma 1"
print "el numero final es : " + str(total2)        

#este codigo corresponde al ejercicio planteado en el final del video
#en este codigo se deben tomar todos los multiplos de 3 y 5, luego se deben sumar y observar si la suma de todos ellos es menor que 100. 
lista3 = []
lista4 = range(1,100) 
for i in lista4: # ciclo que discrimna y agrega numeros multiplos de 3 y 5, desde una lista de numero del 1 hasta 100 sin contar este ultimo.
    if i%3 == 0: #se seleccionan  los numeros multiplos de 3.
       lista3.append(i) #se agregan a lista3
    elif i%5 == 0:#se seleccionan  los numeros multiplos de 3.
        lista3.append(i) #se agregan a lista3.

#print lista3
Suma = 0
    
for i in lista3: #ciclo que suma todos los multiplos de 3 y 5 provenientes de lista3 en Suma.
    Suma +=i
print "la suma de todos los numeros multiplos de 3 y 5 es " + str(Suma)  
if Suma < 100 :
        print str(Suma) +" es menor que 100 "
elif Suma == 100:
        print str(Suma) +" es igual a 100 "
else:
         print str (Suma) + " es mayor a 100 "
         
        

          