# Ejercicio 5: Mini Sistema de Gestión de Inventario

inventario = []

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")


def realizar_venta():
    nombre = input("Ingrese el nombre del producto vendido: ")
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():

            if producto["cantidad"] >= cantidad_vendida:
                producto["cantidad"] = producto["cantidad"] - cantidad_vendida
                print("Venta realizada correctamente.")
            else:
                print("No hay suficiente cantidad disponible.")
            return

    print("Producto no encontrado.")


def mostrar_inventario():

    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("\n--- INVENTARIO ---")

        for producto in inventario:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            print("-" * 30)

while True:
    print("\n----- MENÚ -----")
    print("1. Agregar producto")
    print("2. Realizar venta")
    print("3. Mostrar inventario")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1: 
            agregar_producto()
        case 2:
            realizar_venta()
        case 3:
            mostrar_inventario()
        case 4:
            print("Programa finalizado.")
            break
        case _:
            print("Opcion no válida")