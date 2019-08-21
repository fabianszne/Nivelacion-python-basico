# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:58:22 2019

@author: Fabian
"""
#ciclo while

total = 0
j = 1
while j < 5:  # este ciclo suma el valor de j a total hasta que j es menor a 5, es decir , es 4. Asi, la suma es 1+2+3+4 = 10
    total += j #agrega el valor de j a total.
    j += 1
    
print total    


listaDada = [5,4,4,3,1]
total1= 0
i = 0
while i < len(listaDada) and listaDada[i] > 0: # este ciclo suma los numeros que estan en la listaDada , a total1
     total1 += listaDada[i] 
     i+=1
print total1

# el siguiente codigo es un ciclo for que de una lista toma los numeros y los suma a total2, pero tiene una restriccion que solo le permite sumar los numeros que son positivos, cuando llega a los negativos se detiene.
listaDada2 =  [5,4,4,3,1,-2,-3,-5]
total2 = 0
for ele in listaDada2:
    if ele <= 0: #condicion de tomar solo numeros positivos. Porque de no ser asi, este se detiene y no los suma.
        break
    total2 += ele
    
print total2 

#el siguiente codigo es un ciclo while que realiza la misma accion que el codigo del ciclo for.
listaDada3 = [5,4,4,3,1,-2,-3,-5]
total3 = 0
k= 0
while k <= len(listaDada3) and listaDada3[k] >0:#mientras se cumpla la condicion se podra continur con el ciclo.En el video se utiliza while True, porque es una condicion que siempre se cumple.
    total3 += listaDada3[k]
    k +=1
    if listaDada3[k] <=0:
        break

print total3

#a continuacion se muestra el codigo para el problema propuesto en eñ video

# en este caso, en vez de sumar los numeros positivos , se sumaran solo los negativos.

listaFinal = [8,9,10,5,4,3,-4,-7,-9,1]
# la idea es que la lista este ordenada de menor a mayor. De este modo, con el comando sort() se puede realizar lo anterior.
listaFinal.sort()

print listaFinal
sumaDeNegativos = 0
l = 0 
while True :
    sumaDeNegativos += listaFinal[l]
    l +=1
    if listaFinal[l] >=0:
        break
print sumaDeNegativos

