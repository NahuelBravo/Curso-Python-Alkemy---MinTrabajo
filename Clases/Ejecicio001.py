"""
Consigna: ✍️
Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  Para ellos debemos definir una función que reciba parámetros:
Combinar funciones nativas y funciones definidas,
condicionales, y bucles.
Si el usuario ingresa el nro 1, realiza la acción A.
Si el usuario ingresa el nro 2, realiza la acción B.

"""


def funcion_a(num1, num2):
    return num1 + num2


def funcion_b(num1, num2):
    if num1 == 0 or num2 == 0:
        return f"no se puede dividir por cero"
    else:
        return num1 / num2


def acciones():
    accion = int(input("Ingrese '1' para sumar 2 numeros, "
                       "ingrese '2' para dividir 2 numero,"
                       "ingrese cualquier otro numero para finalizar: "))

    while accion != 1 or accion != 2:
        if accion == 1:
            num1 = int(input("ingrese un numero: "))
            num2 = int(input("ingrese otro numero: "))
            funcion_a(num1, num2)
            print(funcion_a(num1, num2))
            accion = int(input("Ingrese '1' para sumar 2 numeros, "
                               "ingrese '2' para dividir 2 numero,"
                               "ingrese cualquier numero para finalizar: "))
        elif accion == 2:
            num1 = int(input("ingrese un numero: "))
            num2 = int(input("ingrese otro numero: "))
            print(funcion_b(num1, num2))
            accion = int(input("Ingrese '1' para sumar 2 numeros, "
                               "ingrese '2' para dividir 2 numero,"
                               "ingrese cualquier numero para finalizar: "))
        else:
            return False


acciones()
