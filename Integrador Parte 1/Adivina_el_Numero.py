# Adivina el número (juego)
# Crear un programa en el que el usuario deberá adivinar el número que la máquina escogió. 
# Deben utilizar la librería `random` para generar la elección de la máquina. 
# El usuario tendrá 5 vidas, cada vez que intente adivinar, recibirá como respuesta “El número es mayor” o “El número es menor” según corresponda, y perderá una vida. 
# Ganará cuando logre adivinar el número elegido por la máquina.
import random
print("---------------------------------------------------------ADIVINA EL NUMERO------------------------------------------------------")
n2 = random.randint(1,99)

for vidas in range(5,0,-1) :
    condicion = True
    print(f"Tienes {vidas - 1} vidas")
    while condicion:
        n1 = int(input("Ingresa un numero del 1 al 99: "))
        if n1 < 0 or n1 > 99 :
            print("******************************ERROR******************************************")
            print(f"El numero {n1} esta fuera del rango de 1 a 99, ingrese un numero valido")
            print("******************************ERROR******************************************")
        else :
            condicion = False
    
    if n1 > n2 :
        print("El Numero es Menor")
    elif n1 < n2 :
        print("El numero es Mayor")
    
    print("------------------------------------------------------------------------")
    
    if n1 == n2 :
        print(f"{n1} ES EL NUMERO CORRECTO")
        fin = "--------------------------------GANASTE---------------------------------"
        break
    else :
        fin = f"TE QUEDASTE SIN VIDAS EL NUMERO CORRECTO ERA {n2}"
    
print(fin)