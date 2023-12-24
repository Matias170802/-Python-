""" Carrito de compras

Diseñar un programa que simule un carrito de compras, el mismo debe contar con un menú que contenga las siguientes opciones:

1. Agregar producto
2. Eliminar producto
3. Ver lista de compras
4. Finalizar compra
5. Salir

Los productos disponibles son:

Leche $50 - Galletas $35 - Gaseosa $87 - Huevos $66 - Aceite $110 - Pan $20

Al finalizar la compra, debe “imprimirse” el ticket de compra, el cual contendrá la lista de productos y el precio final."""
#------------------------------------------------------INICIO------------------------------------------------------------------------

# Productos y sus precios
productos_disponibles = {
    "Leche": 50,
    "Galletas": 35,
    "Gaseosa": 87,
    "Huevos": 66,
    "Aceite": 110,
    "Pan": 20
}

# Carrito de compras 
carrito = {}

# Función para agregar producto al carrito
def agregar_producto(producto, precio):
    if producto in carrito:
        carrito[producto] += precio
    else:
        carrito[producto] = precio
    print(f"{producto} agregado al carrito.")

# Función para eliminar producto del carrito
def eliminar_producto(producto):
    if producto in carrito:
        del carrito[producto]
        print(f"{producto} eliminado del carrito.")
    else:
        print(f"{producto} no está en el carrito.")

# Función para ver la lista de compras
def ver_lista_compras():
    print("\nLista de Compras:")
    for producto, precio in carrito.items():
        print(f"{producto}: ${precio}")

# Función para finalizar la compra
def finalizar_compra():
    total = sum(carrito.values())
    print(f"\nCompra finalizada. Total a pagar: ${total}")
    ver_lista_compras()

# Menú principal
while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver lista de compras")
    print("4. Finalizar compra")
    print("5. Salir")
    while True :
        opcion = input("Seleccione una opción (1-5): ")
        if opcion in ["1","2","3","4","5"]:
            break
        else :
            print("Opción no válida. Intente de nuevo.")

    if opcion == "1":
        print("\nProductos disponibles:")
        for producto, precio in productos_disponibles.items():
            print(f"{producto}: ${precio}")

        while True :
            producto = input("Ingrese el nombre del producto: ")
            if producto in productos_disponibles:
                agregar_producto(producto, productos_disponibles[producto])
                break
            else:
                print("Producto no válido. Intente de nuevo.")

    elif opcion == "2":
        while True :
            ver_lista_compras()
            producto = input("Ingrese el nombre del producto a eliminar: ")
            if producto in carrito :
                eliminar_producto(producto)
                break
            else :
                print("Producto no válido. Intente de nuevo.")


    elif opcion == "3":
        ver_lista_compras()

    elif opcion == "4":
        finalizar_compra()
        break

    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break

