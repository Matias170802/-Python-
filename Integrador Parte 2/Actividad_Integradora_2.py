#-------------------JUEGO--------------------
import random

#----------------CLASES----------------------

class Personajes :
    def __init__ (self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza


class Guerrero(Personajes) :
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre)
        super().__init__(vida) = 600
        super().__init__(ataque) = 60
        super().__init__(defensa) = 50
        super().__init__(inteligencia) = 20
        super().__init__(agilidad) = 20
        super().__init__(fuerza) = 70 

class Mago(Personajes) :
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre)
        super().__init__(vida) = 350
        super().__init__(ataque) = 35
        super().__init__(defensa) = 30
        super().__init__(inteligencia) = 70
        super().__init__(agilidad) = 40
        super().__init__(fuerza) = 30

class Arquero(Personajes) :
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre)
        super().__init__(vida) = 400
        super().__init__(ataque) = 40
        super().__init__(defensa) = 35
        super().__init__(inteligencia) = 40
        super().__init__(agilidad) = 80
        super().__init__(fuerza) = 30

class Asesino(Personajes) :
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre)
        super().__init__(vida) = 500
        super().__init__(ataque) = 50
        super().__init__(defensa) = 20
        super().__init__(inteligencia) = 55
        super().__init__(agilidad) = 70
        super().__init__(fuerza) = 25

