inventario = {}

def registrar_entrada():
    producto = input("Producto: ")
    cantidad = int(input("Cantidad que ingresa: "))

    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

    print("Entrada registrada")


def registrar_salida():
    producto = input("Producto: ")
    cantidad = int(input("Cantidad que sale: "))

    if producto in inventario and inventario[producto] >= cantidad:
        inventario[producto] -= cantidad
        print("Salida registrada")
    else:
        print("Stock insuficiente")


def calcular_inventario_optimo():

    print("\nNivel de inventario")

    for producto, cantidad in inventario.items():

        if cantidad < 20:
            print(producto, "- Inventario bajo")

        elif cantidad > 100:
            print(producto, "- Exceso de inventario")

        else:
            print(producto, "- Inventario adecuado")


def alerta_reabastecimiento():

    print("\nAlertas")

    for producto, cantidad in inventario.items():

        if cantidad < 20:
            print("Reabastecer:", producto)


def mostrar_inventario():

    print("\nInventario actual")

    for producto, cantidad in inventario.items():
        print(producto, ":", cantidad)


def menu():

    while True:

        print("\n===== INVENTARIO =====")
        print("1 Registrar entrada")
        print("2 Registrar salida")
        print("3 Ver inventario")
        print("4 Nivel óptimo")
        print("5 Alertas")
        print("0 Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_entrada()

        elif opcion == "2":
            registrar_salida()

        elif opcion == "3":
            mostrar_inventario()

        elif opcion == "4":
            calcular_inventario_optimo()

        elif opcion == "5":
            alerta_reabastecimiento()

        elif opcion == "0":
            break


menu()