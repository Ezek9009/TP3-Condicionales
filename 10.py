"""
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano.

"""
hemisferio = input("en que hemisferio se encuentra ? (N/S): ").lower()
mes = int(input("que mes del año es?: "))
dia = int(input("ingrese dia del mes: "))

#Hemisferio norte:
if hemisferio == 'n':
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en la estacion de invierno.")

    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en la estacion de primavera.")

    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en la estacion de verano.")
        
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en la estacion de otoño.")

#Hemisferio sur:
if hemisferio == 's':
    if(mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        print("Se encuentra en la estacion de verano.")

    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        print("Se encuentra en la estacion de otoño.")

    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        print("Se encuentra en la estacion de invierno.")

    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        print("Se encuentra en la estacion de primavera.")

    else:
        print("Hemisferio ingresado no válido. Por favor ingrese 'N' para norte o 'S' para sur")
    