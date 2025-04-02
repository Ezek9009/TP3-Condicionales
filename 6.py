"""
6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
siguiente:
from statistics import mode, median, mean 
mi_lista = [1,2,5,5,3] 
mean(mi_lista)
En la documentación oficial se puede encontrar más información sobre este paquete: 
https://docs.python.org/es/3.8/library/statistics.html.  
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se 
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio: 
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales. 
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
Definir la lista numeros_aleatorios de la siguiente forma:
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
forma aleatoria.

"""
from statistics import mode, median, mean 
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50) ]

#asignamos la funcion mode a moda
#(indica que numero se repite en la lista)
moda = mode(numeros_aleatorios)

#asignamos la funcion median a mediana
#(retorna el valor del medio de la lista si es impar
#si es par,se toman los 2 valores centrales se los suma y se dividen por 2)
mediana = median(numeros_aleatorios)

#asignamos la funcion mean a media
#(la media es el promedio de los valores de la lista)
media = mean(numeros_aleatorios)

#Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
#mediana es mayor que la moda.
if media > mediana and mediana > moda:
    print("sesgo positivo")
    
#Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
#la mediana es menor que la moda.
elif media < mediana and mediana < moda:
    print("sesgo negativo")

#Sin sesgo: cuando la media, la mediana y la moda son iguales.
elif media == mediana == moda:
    print("no hay sesgo")