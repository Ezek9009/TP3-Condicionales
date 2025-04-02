"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. 
"""
#pedimos al usuario que ingrese una frase y lo 
#guardamos en la variable frase
frase = input("ingrese una frase o palabra: ")

#creo la variable vocales para comparar si 
#hay vocales en el ultimo subindice de la variable frase
vocales = "aeiouAEIOU"

#frase[-1] verifica en el ultimo subindice de frase
#si hay vocal, se agrega ! al final de la cadena
#en caso contrario se imprime normalmente
if frase[-1] in vocales:
    print(f"{frase}!")
else:
    print(frase)