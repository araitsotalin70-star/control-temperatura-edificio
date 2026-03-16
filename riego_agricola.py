# ==========================================
# SISTEMA DE RIEGO AUTOMATIZADO
# ==========================================

import random

humedad_suelo = 0
clima = "desconocido"


# -----------------------------------------
# Función para leer sensores de humedad
# -----------------------------------------
def leer_humedad():

    global humedad_suelo

    humedad_suelo = random.randint(10, 90)

    print("\nHumedad del suelo:", humedad_suelo, "%")


# -----------------------------------------
# Función para consultar previsión clima
# -----------------------------------------
def consultar_clima():

    global clima

    clima = random.choice(["soleado", "nublado", "lluvia"])

    print("\nPrevisión meteorológica:", clima)


# -----------------------------------------
# Procedimiento para calcular riego óptimo
# -----------------------------------------
def calcular_riego():

    print("\nCalculando cantidad de riego...")

    if humedad_suelo < 30 and clima != "lluvia":
        print("Aplicar riego alto")

    elif humedad_suelo < 50:
        print("Aplicar riego moderado")

    else:
        print("No es necesario regar")


# -----------------------------------------
# Función para controlar válvulas
# -----------------------------------------
def controlar_valvulas():

    secciones = ["Sección A", "Sección B", "Sección C"]

    print("\nControl de válvulas")

    for seccion in secciones:

        estado = random.choice(["abierta", "cerrada"])

        print(seccion, "válvula", estado)


# -----------------------------------------
# MENÚ DEL SISTEMA
# -----------------------------------------
def menu():

    while True:

        print("\n===== SISTEMA DE RIEGO =====")
        print("1 Leer humedad del suelo")
        print("2 Consultar clima")
        print("3 Calcular riego óptimo")
        print("4 Controlar válvulas")
        print("0 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            leer_humedad()

        elif opcion == "2":
            consultar_clima()

        elif opcion == "3":
            calcular_riego()

        elif opcion == "4":
            controlar_valvulas()

        elif opcion == "0":
            print("Sistema finalizado")
            break

        else:
            print("Opción inválida")


menu()