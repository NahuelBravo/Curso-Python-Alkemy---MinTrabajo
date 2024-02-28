"""
3. A partir del siguiente enunciado, crear las clases necesarias (con
sus respectivos atributos y métodos) para poder representarlos.
↪ “Juan Lopez tiene 25 años y es de profesión Abogado. Por la
tarde, después de trabajar, sale a caminar. También tiene una
bicicleta amarilla marca “Massino” y a veces sale a dar
vueltas en ella”.
"""
class Persona():
    def __init__(self, nombre:str, apellido:str, profesion: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.profesion = profesion
        self.bicicleta = Bicicleta()

    
    def caminar(self):
        return f"{self.nombre}{self.apellido} esta caminando"
    
    def __str__(self) -> str:
        return f"{self.nombre}{self.apellido}"
    
    def andar_en_bicicleta(self):
        return f"{self.nombre} {self.apellido} {self.bicicleta.andar()} en bicicleta"

    
class Bicicleta():
    def __init__(self, color = "Azul", marca = "", rodado = 23) -> None:
        self.color = color
        self.marca = marca
        self.rodado = rodado
    
    def color(self):
        return self.color
    
    def marca(self):
        return self.marca
    
    def rodado(self):
        return self.rodado
    
    def andar(self):
        return "Estoy andando"
    
    def __str__(self) -> str:
        return f"{self.color}, {self.marca}, {self.rodado}"
    

# Instancia de Bicicleta
bicicleta_juan = Bicicleta(color="Amarilla", marca="Massino", rodado=23)

# Instancia de Persona
juan_lopez = Persona(nombre="Juan", apellido="Lopez", profesion="Abogado")
juan_lopez.bicicleta = bicicleta_juan  # Asignamos la bicicleta a Juan

# Probamos los métodos
print(juan_lopez.caminar())
print(juan_lopez.andar_en_bicicleta())
