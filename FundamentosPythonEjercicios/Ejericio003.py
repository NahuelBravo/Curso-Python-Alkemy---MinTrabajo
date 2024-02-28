"""
3. Crea una función llamada verificar_calificacion que reciba tres
parámetros: nota1, nota2 y nota3
↪ Dentro de la función calcular el promedio de notas
↪ Si el promedio es mayor o igual a 6, entonces la función debe
retornar un mensaje “Aprobado”, en caso contrario
“Reprobado”
"""
nota1 = int(input("ingrese nota 1: "))
nota2 = int(input("ingrese nota 2: "))
nota3 = int(input("ingrese nota 3: "))

def verificar_calificacion(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3)/3
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Reprobado"

print(verificar_calificacion(nota1,nota2,nota3))