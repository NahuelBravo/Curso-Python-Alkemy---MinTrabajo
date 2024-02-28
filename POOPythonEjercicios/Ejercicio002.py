"""
2. Crear una clase llamada Animal, otra llamada Perro y otra llamada
Águila.
↪ La clase Animal tiene:
○ atributo cantidad_patas: numérico
○ atributo tipo: vertebrado/invertebrado
○ método comer(): retorna un string “estoy comiendo”
↪ La clase Perro hereda de Animal y agrega:
○ atributo nombre: texto
○ atributo raza: texto
○ método correr(): retorna un string “estoy corriendo”
↪ La clase Aguila hereda de Animal y agrega:
○ método volar(): retorna un string “estoy volando”
"""

class Animal():
    def __init__(self, cantidad_patas:int , tipo:str):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return "Estoy Comiendo"
    
    def __str__(self) -> str:
        return f"Cantidad de Patas: {self.cantidad_patas}, Tipo: {self.tipo}"

class Perro(Animal):
    def __init__(self, cantidad_patas: int, tipo: str, nombre:str, raza:str):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    
    def correr(self):
        return "Estoy Corriendo"
    
    def __str__(self) -> str:
        return f"{super().__str__()}, {self.nombre}, {self.raza}"
    
class Aguila(Animal):
    def __init__(self, cantidad_patas: int, tipo: str):
        super().__init__(cantidad_patas, tipo)
    
    def volar(self):
        return "Estoy volando"
    
    def __str__(self) -> str:
        return super().__str__()


animal_generico = Animal(cantidad_patas=4, tipo="vertebrado")
print("Animal:")
print(animal_generico)
print(animal_generico.comer())
print("\n")

# Instancia de Perro
perro = Perro(cantidad_patas=4, tipo="vertebrado", nombre="Max", raza="Labrador")
print("Perro:")
print(perro)
print(perro.comer())
print(perro.correr())
print("\n")

# Instancia de Águila
aguila = Aguila(cantidad_patas=2, tipo="vertebrado")
print("Águila:")
print(aguila)
print(aguila.comer())
print(aguila.volar())