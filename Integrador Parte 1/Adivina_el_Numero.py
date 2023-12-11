# Adivina el número (juego)
# Crear un programa en el que el usuario deberá adivinar el número que la máquina escogió. 
# Deben utilizar la librería `random` para generar la elección de la máquina. 
# El usuario tendrá 5 vidas, cada vez que intente adivinar, recibirá como respuesta “El número es mayor” o “El número es menor” según corresponda, y perderá una vida. 
# Ganará cuando logre adivinar el número elegido por la máquina.
import random
print("---------------------------------------------------------ADIVINA EL NUMERO------------------------------------------------------")
n2 = random.randint(1,99)

for vidas in range(5,0,-1) :
    
    print(n2)
    n1 = int(input("Ingresa un numero del 1 al 99: "))
    if n1 == n2 :
        print(f"{n1} ES EL NUMERO CORRECTO")
        break
    if n1 > n2 :
        print("El Numero es Menor")
    else :
        print("El numero es Mayor")
    print(vidas)
print()