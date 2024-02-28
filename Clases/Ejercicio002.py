"""
Enunciado
Cierta empresa requiere una aplicación informática
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo,
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo.

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa:
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""
from enum import Enum


class Empleado:

    def __init__(self, dni, nombre, apellido, anio_ingreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso

    def calcular_salario(self):
        pass

    def mostrar_salario(self):
        return self.calcular_salario()


class EmpleadoComision(Empleado):

    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo, clientes_captados, monto_por_cliente):
        super().__init__(dni=dni, nombre=nombre, apellido=apellido, anio_ingreso=anio_ingreso)
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.monto_por_cliente = monto_por_cliente

    def calcular_salario(self):
        calculo_salario = self.clientes_captados * self.monto_por_cliente
        if calculo_salario < self.salario_minimo:
            return f"{self.salario_minimo}"
        else:
            return f"{calculo_salario}"


class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anio_ingreso, salario_minimo):
        super().__init__(dni=dni, nombre=nombre, apellido=apellido, anio_ingreso=anio_ingreso)
        self.salario_minimo = salario_minimo

    def calcular_salario(self):
        if self.anio_ingreso > 5:
            return f"{self.salario_minimo + (self.salario_minimo * 0.1)}"
        elif self.anio_ingreso >= 2 and self.anio_ingreso >= 5:
            return f"{self.salario_minimo + (self.salario_minimo * 0.05)}"
        else:
            return f"{self.salario_minimo}"


empleado_comision_1 = EmpleadoComision(dni=1, nombre="Juan", apellido="Perez", anio_ingreso=2019,
                                       salario_minimo=2000, clientes_captados=20, monto_por_cliente=100)
empleado_comision_2 = EmpleadoComision(dni=3, nombre="Ana", apellido="Lopez", anio_ingreso=2020,
                                       salario_minimo=1800, clientes_captados=15, monto_por_cliente=120)
empleado_comision_3 = EmpleadoComision(dni=5, nombre="Laura", apellido="Martinez", anio_ingreso=2018,
                                       salario_minimo=2200, clientes_captados=25, monto_por_cliente=90)
empleado_salario_fijo_3 = EmpleadoSalarioFijo(dni=6, nombre="Pedro", apellido="Garcia", anio_ingreso=2016,
                                              salario_minimo=2800)
empleado_salario_fijo_1 = EmpleadoSalarioFijo(dni=2, nombre="Maria", apellido="Gomez", anio_ingreso=2017,
                                              salario_minimo=2500, )
empleado_salario_fijo_2 = EmpleadoSalarioFijo(dni=4, nombre="Carlos", apellido="Rodriguez", anio_ingreso=2015,
                                              salario_minimo=3000)


# Mostrar salarios

print(empleado_comision_1.mostrar_salario())
print(empleado_comision_2.mostrar_salario())
print(empleado_comision_3.mostrar_salario())

print(empleado_salario_fijo_1.mostrar_salario())
print(empleado_salario_fijo_2.mostrar_salario())
print(empleado_salario_fijo_3.mostrar_salario())
