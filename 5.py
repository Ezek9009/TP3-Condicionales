"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
como una lista o un string.
"""
contraseña = input("ingrese contraseña entre 8 y 14 caracteres: ")

#la funcion len(contraseña) devuelve la longitud(length) de la variable
#contraseña, si es entre 8 y 14 es correcta
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")

#en caso contrario es incorrecta
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")