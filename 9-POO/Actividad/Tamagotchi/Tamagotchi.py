class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"{self.nombre}:")
        print(f"Nivel de Energía: {self.nivel_energia}")
        print(f"Nivel de Hambre: {self.nivel_hambre}")
        print(f"Estado de Humor: {self.humor}")
        print()

    def alimentar(self):
        self.nivel_hambre -= 10
        self.nivel_energia -= 15
        self.verificar_estado()

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10
        self.verificar_estado()

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5
        self.verificar_estado()

    def verificar_estado(self):
        if self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30

        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha muerto.")
        else:
            self.actualizar_humor()

    def actualizar_humor(self):
        if self.nivel_felicidad >= 80:
            self.humor = "eufórico"
        elif 50 <= self.nivel_felicidad < 80:
            self.humor = "feliz"
        elif 20 <= self.nivel_felicidad < 50:
            self.humor = "indiferente"
        elif 0 <= self.nivel_felicidad < 20:
            self.humor = "triste"
        elif self.nivel_felicidad < 0:
            self.nivel_felicidad = 0

mi_tamagotchi = Tamagotchi("Tammy")
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.alimentar()
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.jugar()
mi_tamagotchi.mostrar_estado()
mi_tamagotchi.dormir()
mi_tamagotchi.mostrar_estado()