"""
1. Crear un algoritmo para calcular la sumatoria de los primeros cien
números (del 01 al 100) con un ciclo while.
"""

def calcular_1_al_100():
    contador = 0
    suma = 0
    while contador <= 100:
        suma += contador        
        contador +=1
        print(suma)

calcular_1_al_100()