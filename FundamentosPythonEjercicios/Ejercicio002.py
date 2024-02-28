"""
2. Crear una lista con 5 elementos y luego aplica los siguientes
accionables:
↪ Imprimir el último elemento
↪ Modificar el valor del tercer elemento
↪ Agregar dos elementos
↪ Eliminar algún elemento
"""

list1 = [50,30,40,70,80]
print(list1[-1])
list1[2] = "hola"
print(list1[2])
list1.append("chau")
list1.append("340")
print(list1)
list1.pop(0)
print(list1)
