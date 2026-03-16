# ==========================================
# SISTEMA DE NAVEGACIÓN VEHÍCULO AUTÓNOMO
# ==========================================

import random

# Variables simuladas del sistema
distancia_obstaculo = 100
velocidad = 60


# ------------------------------------------
# Función para leer sensores
# ------------------------------------------
def leer_sensores():

    global distancia_obstaculo

    # Simula datos de sensores de proximidad
    distancia_obstaculo = random.randint(5, 100)

    print("\nLectura de sensores")
    print("Distancia al obstáculo:", distancia_obstaculo, "metros")


# ------------------------------------------
# Procedimiento para calcular ruta óptima
# ------------------------------------------
def calcular_ruta():

    print("\nCalculando ruta óptima...")

    rutas = ["Ruta A - autopista", "Ruta B - avenida principal", "Ruta C - calle secundaria"]

    ruta_optima = random.choice(rutas)

    print("Ruta seleccionada:", ruta_optima)


# ------------------------------------------
# Función para detectar y evitar obstáculos
# ------------------------------------------
def evitar_obstaculos():

    global distancia_obstaculo

    print("\nSistema de detección de obstáculos")

    if distancia_obstaculo < 20:
        print("⚠ Obstáculo detectado")
        print("El vehículo cambia de carril")

    else:
        print("Camino libre")


# ------------------------------------------
# Procedimiento para ajustar velocidad
# ------------------------------------------
def ajustar_velocidad():

    global velocidad
    trafico = random.choice(["bajo", "medio", "alto"])

    print("\nCondición del tráfico:", trafico)

    if trafico == "alto":
        velocidad = 30

    elif trafico == "medio":
        velocidad = 50

    else:
        velocidad = 80

    print("Velocidad ajustada a:", velocidad, "km/h")


# ------------------------------------------
# Menú del sistema
# ------------------------------------------
def menu():

    while True:

        print("\n===== SISTEMA VEHÍCULO AUTÓNOMO =====")
        print("1 Leer sensores")
        print("2 Calcular ruta óptima")
        print("3 Detectar obstáculos")
        print("4 Ajustar velocidad")
        print("0 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            leer_sensores()

        elif opcion == "2":
            calcular_ruta()

        elif opcion == "3":
            evitar_obstaculos()

        elif opcion == "4":
            ajustar_velocidad()

        elif opcion == "0":
            print("Sistema detenido")
            break

        else:
            print("Opción inválida")


menu()