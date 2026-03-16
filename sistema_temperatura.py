import random
from datetime import datetime

# -------------------------------------------------------
# FUNCION: leer_sensores_temperatura
# Simula la lectura de sensores en distintas zonas
# del edificio inteligente.
# -------------------------------------------------------
def leer_sensores_temperatura():

    sensores = {
        "Zona Norte": round(random.uniform(18, 28), 2),
        "Zona Sur": round(random.uniform(18, 28), 2),
        "Zona Este": round(random.uniform(18, 28), 2),
        "Zona Oeste": round(random.uniform(18, 28), 2)
    }

    return sensores


# -------------------------------------------------------
# FUNCION: calcular_temperatura_optima
# Calcula la temperatura ideal considerando:
# hora, ocupación y temperatura exterior.
# -------------------------------------------------------
def calcular_temperatura_optima(hora, ocupacion, temp_exterior):

    temperatura_base = 22

    if ocupacion > 50:
        temperatura_base -= 1

    if temp_exterior > 30:
        temperatura_base = 20
    elif temp_exterior < 10:
        temperatura_base = 24

    if hora >= 22 or hora <= 6:
        temperatura_base -= 2

    return temperatura_base


# -------------------------------------------------------
# PROCEDIMIENTO: enviar_ajuste_climatizacion
# Ajusta calefacción o refrigeración según la temperatura
# -------------------------------------------------------
def enviar_ajuste_climatizacion(zona, temp_actual, temp_optima):

    if temp_actual > temp_optima:
        print(f"{zona}: Activar refrigeración")
    elif temp_actual < temp_optima:
        print(f"{zona}: Activar calefacción")
    else:
        print(f"{zona}: Temperatura adecuada")


# -------------------------------------------------------
# FUNCION: registrar_consumo_energia
# Registra consumo energético y calcula promedio
# -------------------------------------------------------
def registrar_consumo_energia(consumo_actual, historial):

    historial.append(consumo_actual)
    promedio = sum(historial) / len(historial)

    return promedio


# -------------------------------------------------------
# FUNCION: mostrar_menu
# Muestra las opciones del sistema
# -------------------------------------------------------
def mostrar_menu():

    print("\n===== SISTEMA DE CONTROL DE TEMPERATURA =====")
    print("1. Leer sensores de temperatura")
    print("2. Calcular temperatura óptima")
    print("3. Ajustar climatización")
    print("4. Registrar consumo energético")
    print("5. Ejecutar sistema completo")
    print("0. Salir")


# -------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------
def main():

    historial_consumo = []
    sensores = {}
    temp_optima = 22

    while True:

        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            sensores = leer_sensores_temperatura()
            print("\nTemperaturas actuales:")
            for zona, temp in sensores.items():
                print(zona, ":", temp, "°C")

        elif opcion == "2":

            hora = datetime.now().hour
            ocupacion = random.randint(10, 100)
            temp_exterior = random.uniform(5, 35)

            temp_optima = calcular_temperatura_optima(
                hora,
                ocupacion,
                temp_exterior
            )

            print("\nHora actual:", hora)
            print("Ocupación:", ocupacion)
            print("Temperatura exterior:", round(temp_exterior,2))
            print("Temperatura óptima:", temp_optima)

        elif opcion == "3":

            if not sensores:
                print("Primero debe leer los sensores.")
            else:
                print("\nAjuste del sistema de climatización")
                for zona, temp in sensores.items():
                    enviar_ajuste_climatizacion(zona, temp, temp_optima)

        elif opcion == "4":

            consumo = random.uniform(100, 300)

            promedio = registrar_consumo_energia(
                consumo,
                historial_consumo
            )

            print("\nConsumo actual:", round(consumo,2))
            print("Consumo promedio:", round(promedio,2))

        elif opcion == "5":

            sensores = leer_sensores_temperatura()

            hora = datetime.now().hour
            ocupacion = random.randint(10, 100)
            temp_exterior = random.uniform(5, 35)

            temp_optima = calcular_temperatura_optima(
                hora,
                ocupacion,
                temp_exterior
            )

            print("\nTemperatura óptima:", temp_optima)

            for zona, temp in sensores.items():
                enviar_ajuste_climatizacion(zona, temp, temp_optima)

        elif opcion == "0":

            print("Saliendo del sistema...")
            break

        else:

            print("Opción inválida")


# Ejecutar programa
main()