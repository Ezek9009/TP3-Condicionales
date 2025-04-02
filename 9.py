"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""

mTerremoto = int(input("ingrese magnitud del terremoto: "))

#Menor que 3: "Muy leve" (imperceptible).
if mTerremoto < 3:
    print("Muy leve (imperceptible)")

#Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
elif mTerremoto >= 3 and mTerremoto < 4:
    print("Leve (ligeramente perceptible)")

#Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños).    
elif mTerremoto >= 4 and mTerremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")

#Mayor o igual que 5  y menor que 6:
#"Fuerte" (puede causar daños en estructuras 
#débiles).
elif mTerremoto >= 5 and mTerremoto < 6:
    print("Fuerte (puede causar daños de estructuras débiles)")

#Mayor o igual que 6  y menor que 7:
#"Muy Fuerte" (puede causar daños significativos).
elif mTerremoto >= 6 and mTerremoto < 7:
    print("Muy fuerte (puede causar daños significativos)")

#Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).    
elif mTerremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")    
