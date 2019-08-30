# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:25:45 2019

@author: Fabian
"""


from matplotlib import pyplot as plt
plt.xkcd() #otro tipo de estilo para el grafico
#plt.style.use('fivethirtyeight') #estilo diferente del grafico.
print plt.style.available #uestraestilos de graficos que alusarlos hacen un poco mas bonito todo.
#listas , una posee lo que sera el eje x y la otra el eje y.

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y =[38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928,67317, 68748, 73752]

plt.plot(ages_x,dev_y, 'k--', label = ' All Devs')
#plt.plot(ages_x,dev_y, color ='k', linestyle = '--' label = ' All Devs')# esta es una forma mas entendible que lo anterior.



#py_dev_x = [25,26,27,28,29,30,31,32,33,34,35]
py_dev_y = [45372, 48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]

plt.plot(ages_x,py_dev_y,'r' ,linewidth = 3, marker= 'o',label = 'Python' )
#linewidth engros la linea del grafico

#plt.plot(dev_x,dev_y)# generamos un grafico con los valores en los ejes correspondientes.
plt.xlabel('Ages') #leyenda que va en el eje x
plt.ylabel('Median Salary (USD)') #leyenda que va en el eje y
plt.title( 'Median Salary (USD) by Age')

plt.savefig('plot.png')
plt.legend() #genera leyenda en el intetrior del grafico y permite conocer a que ddato pertence cada curva.
#es posible generar la leyenda en el plt.plot dejando plt.legends vacio,
#y agregando label = ' ' , se genera la leyenda 
plt.grid(True)
plt.tight_layout()
plt.show()


