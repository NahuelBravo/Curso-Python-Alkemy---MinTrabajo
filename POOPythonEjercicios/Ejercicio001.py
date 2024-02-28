"""
1. Crear una clase llamada Bicicleta y luego aplica los siguientes
accionables:
↪ Agregar al menos 3 atributos
↪ Agregar al menos 3 métodos
↪ Agregar el método constructor de la clase.
"""

class Bicicleta():
    def __init__(self, color, marca, rodado) -> None:
        self.color = color
        self.marca = marca
        self.rodado = rodado
    
    def color(self):
        return self.color
    
    def marca(self):
        return self.marca
    
    def rodado(self):
        return self.rodado
    
    def __str__(self) -> str:
        return f"{self.color}, {self.marca}, {self.rodado}"
    
b1 = Bicicleta("Rojo", "Olmo", 23)

print(b1)