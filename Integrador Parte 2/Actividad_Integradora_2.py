#-------------------JUEGO--------------------
import random

#----------------CLASES----------------------

class Personajes :
    def __init__ (self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
    def Atacar():
        pass
    def Arma():
        pass
    def Atributos():
        pass
    def Habilidades():
        pass

#------------------------------------------------
#------------------HEROES------------------------
#------------------------------------------------

class Guerrero(Personajes) :
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)
        print("----------PERSONAJE ELEGIDO-----------")
        print(" GUERRERO ")

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)
    
    def Atacar(self) : 
        print("ATAQUE !!!")
    
    def Arma(self) :
        print("""
 ------------------------ELIGE TU ARMA--------------------------
|Estos son los atributos que te daran cada una, elije sabiamente|
| ESPADA              HACHA                                     |
| Ataque +30          Ataque +50                                |
| Defesa +20          Defensa +15                               |
| Agilidad -10        Agilidad -20                              |
----------------------------------------------------------------
            """)
        while True :
            eleccion = input("Elije ESPADA o HACHA para tu batalla: ")
            if eleccion.lower() in ["espada","hacha"] :
                eleccion = eleccion.lower()
                break
            else : 
                print("**************************")
                print("Error vuelve a intentarlo ")
                print("**************************")
        if eleccion == "espada":
            self.ataque += 30
            self.defensa += 20
            self.agilidad -= 10
        elif eleccion == "hacha" :
            self.ataque += 50
            self.defensa += 15
            self.agilidad -= 20

    def Habilidades():
        pass

class Mago(Personajes) :
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)
        print("----------PERSONAJE ELEGIDO-----------")
        print(" MAGO ")
    
    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)
    
    def Atacar(self) : 
        print("MAGIA !!!")
    
    def Arma(self) :
        print("""
 ------------------------ELIGE TU ARMA--------------------------
|Estos son los atributos que te daran cada una, elije sabiamente|
| BASTON DE CRISTAL     POSIONES                                |
| Ataque +20            Ataque +20 x3                           |
| Defesa +30            Defensa +0                              |
| Agilidad -10          Agilidad +20                            |
----------------------------------------------------------------
            """)
        while True :
            eleccion = input("Elije BASTON DE CRISTAL o POSIONES para tu batalla: ")
            if eleccion.lower() in ["baston de cristal","posiones"] :
                eleccion = eleccion.lower()
                break
            else : 
                print("**************************")
                print("Error vuelve a intentarlo ")
                print("**************************")
        if eleccion == "baston de cristal":
            self.ataque += 20
            self.defensa += 30
            self.agilidad -= 10
        elif eleccion == "posiones" :
            self.ataque += 20 #por tres, que en las siguientes 3 turnos le saque 20 en cada uno
            self.defensa += 0
            self.agilidad += 20


class Arquero(Personajes) :
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)
        print("----------PERSONAJE ELEGIDO-----------")
        print(" ARQUERO ")

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)
    def Atacar(self) : 
        print("Flechasss !!!")
    
    def Arma(self) :
        print("""
 ------------------------ELIGE TU ARMA--------------------------
|Estos son los atributos que te daran cada una, elije sabiamente|
| ARCO                BALLESTA                                  |
| Ataque +30          Ataque +40                                |
| Defesa +10          Defensa -10                               |
| Agilidad +20        Agilidad +10                              |
----------------------------------------------------------------
            """)
        while True :
            eleccion = input("Elije ARCO o BALLESTA para tu batalla: ")
            if eleccion.lower() in ["arco","ballesta"] :
                eleccion = eleccion.lower()
                break
            else : 
                print("**************************")
                print("Error vuelve a intentarlo ")
                print("**************************")
        if eleccion == "arco":
            self.ataque += 30
            self.defensa += 10
            self.agilidad += 20
        elif eleccion == "ballesta" :
            self.ataque += 40
            self.defensa -= 10
            self.agilidad += 10


class Asesino(Personajes) :
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)
        print("----------PERSONAJE ELEGIDO-----------")
        print(" ASESINO ")
    
    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)
    
    def Atacar(self) : 
        print("MUERTEE !!!")
    
    def Arma(self) :
        print("""
 ------------------------ELIGE TU ARMA--------------------------
|Estos son los atributos que te daran cada una, elije sabiamente|
| DAGA                CUCHILLOS ARROJADIZOS                     |
| Ataque +60          Ataque +30 x2                             |
| Defesa -20          Defensa -10                               |
| Agilidad +40        Agilidad +30                              |
----------------------------------------------------------------
            """)
        while True :
            eleccion = input("Elije DAGA o CUCHILLOS ARROJADIZOS para tu batalla: ")
            if eleccion.lower() in ["daga","cuchillos arrojadizos"] :
                eleccion = eleccion.lower()
                break
            else : 
                print("**************************")
                print("Error vuelve a intentarlo ")
                print("**************************")
        if eleccion == "daga":
            self.ataque += 60
            self.defensa -= 20
            self.agilidad += 40
        elif eleccion == "cuchillos arrojadizos" :
            self.ataque += 30 #por 2 deberia tirar 2 cuchillos
            self.defensa -= 10
            self.agilidad += 30


#--------------------------------
#------------ENEMIGOS------------
#--------------------------------


class Ogro(Personajes):
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)

class Dragon(Personajes):
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)

class MagoOscuro(Personajes):
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)

class Esqueleto(Personajes):
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)

class Duende(Personajes):
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)

class Gusano(Personajes):
    def __init__(self,nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza):
        super().__init__(nombre,vida,ataque,defensa,inteligencia,agilidad,fuerza)

    def Atributos(self) :
        print(f"""
--------ATRIBUTOS---------
Nombre :{self.nombre} 
Vida: {self.vida}
Ataque: {self.ataque}
Defensa: {self.defensa}
Inteligencia: {self.inteligencia}
Agilidad: {self.agilidad}
Fuerza: {self.fuerza}
        """)

#--------------------------------
#-------------MAIN---------------
#--------------------------------


nombre = input("Ingresa el nombre de tu Heroe: ")
while True :
    tipo = input("Elige que Heroe seras: [Guerrero, Mago, Arquero, Asesino]: ")
    if tipo.lower() in ["guerrero", "mago", "arquero", "asesino"]:
        tipo = tipo.lower()
    else :
        print("**************************")
        print("Error vuelve a intentarlo ")
        print("**************************")
    if tipo == "guerrero" :
        heroe = Guerrero(nombre,600,60,50,20,20,70)
        break
    elif tipo == "mago" :
        heroe = Mago(nombre,350,35,30,70,40,30)
        break
    elif tipo == "arquero" :
        heroe = Arquero(nombre,400,40,35,40,80,30)
        break
    elif tipo == "asesino" :
        heroe = Asesino(nombre,500,50,20,55,70,25)
        break

heroe.Atributos()
heroe.Arma()
print("""
Excelente eleccion tus nuevos atributos son:
""")
heroe.Atributos()
heroe.Habilidades()

