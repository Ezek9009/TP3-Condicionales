"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""
#nombre del usuario
nombre = input("ingrese su nombre: ")

#menu para seleccionar si quiere su nombre en mayusculas, minusculas
#o solo la primer letra en mayusculas
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n"
"2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. \n"
"3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n")

#ingreso de seleccion
numero = int(input("ingrese su numero: "))

#si numero es igual a 1 se imprime todo el nombre en MAYUSCULAS
if numero == 1:
    print(nombre.upper())

#si numero es igual a 2 se imprime todo el nombre en minusculas
elif numero == 2:
    print(nombre.lower())

#si numero es igual a 3 se imprime en MAYUSCULAS solo el primer
#caracter del nombre
elif numero == 3:
    print(nombre.title())