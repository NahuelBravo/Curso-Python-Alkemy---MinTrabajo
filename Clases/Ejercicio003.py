"""


"""

from enum import Enum


class Fabrica:
    def __init__(self):
        self.sucursales = []

    def agregarSucursal(self, sucursal):
        self.sucursales.append(sucursal)

    def mostarSucursales(self):
        sucursales = {}
        for sucursal in self.sucursales:
            nombre_sucursal = sucursal.nombre
            instrumentos_sucursal = sucursal.mostrarInstrumentos()
            sucursales[nombre_sucursal] = instrumentos_sucursal

        for nombre_sucursal, instrumentos_sucursal in sucursales.items():
            print(f"\n Nombre Sucursal: {nombre_sucursal}")
            print(f"\n Instrumentos:\n {instrumentos_sucursal}")


class Sucursal:

    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    def mostrarInstrumentos(self):
        listaInstrumentos = []
        for instrumento in self.instrumentos:
            listaInstrumentos.append(str(instrumento))
        return "\n \n".join(listaInstrumentos)

    def mostrarTipoInstrumentos(self, tipo):
        listaTipoInstrumentos = []
        for instrumento in self.instrumentos:
            if instrumento.tipo == tipo:
                listaTipoInstrumentos.append(str(instrumento))

        return "\n \n".join(listaTipoInstrumentos)

    def __str__(self):
        return f"Sucursal: {self.nombre}\n{self.mostrarInstrumentos()}"


class TipoInstrumento(Enum):
    VIENTO = 1
    CUERDA = 2
    PERCUSION = 3


class Instrumento:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Precio: {self.precio}")


fabrica = Fabrica()

sucursal1 = Sucursal("Sucursal A")
sucursal2 = Sucursal("Sucursal B")

fabrica.agregarSucursal(sucursal1)
fabrica.agregarSucursal(sucursal2)

instrumento1 = Instrumento("Flauta", 100, TipoInstrumento.VIENTO)
instrumento2 = Instrumento("Guitarra", 200, TipoInstrumento.CUERDA)
instrumento3 = Instrumento("Batería", 300, TipoInstrumento.PERCUSION)
instrumento4 = Instrumento("Saxofón", 150, TipoInstrumento.VIENTO)
instrumento5 = Instrumento("Violín", 250, TipoInstrumento.CUERDA)
instrumento6 = Instrumento("Tambor", 350, TipoInstrumento.PERCUSION)
instrumento7 = Instrumento("Flauta", 100, TipoInstrumento.VIENTO)

sucursal1.agregarInstrumento(instrumento1)
sucursal1.agregarInstrumento(instrumento2)
sucursal1.agregarInstrumento(instrumento3)
sucursal1.agregarInstrumento(instrumento7)
sucursal2.agregarInstrumento(instrumento4)
sucursal2.agregarInstrumento(instrumento5)
sucursal2.agregarInstrumento(instrumento6)

print("Información de la Fábrica:")
print(fabrica.mostarSucursales())

print("\nInformación de las Sucursales:")
print(sucursal1)
print("\n------------------------------")
print(sucursal2)
print("----------------------------------------------------------")
print("tipos de instrumentos \n \n")
print(sucursal1.mostrarTipoInstrumentos(TipoInstrumento.VIENTO))
print(sucursal2.mostrarTipoInstrumentos(TipoInstrumento.CUERDA))