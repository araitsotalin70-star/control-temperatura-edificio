# ==========================================
# SISTEMA DE OPTIMIZACIÓN DE PRODUCCIÓN
# ==========================================

import random

# Datos simulados
maquinas = {
    "Maquina1": "activa",
    "Maquina2": "activa",
    "Maquina3": "activa"
}

produccion_diaria = []


# ----------------------------------------
# Función para monitorear el estado máquinas
# ----------------------------------------
def monitorear_maquinas():

    print("\nEstado de las máquinas")

    for maquina in maquinas:

        estado = random.choice(["activa", "mantenimiento", "detenida"])
        maquinas[maquina] = estado

        print(maquina, ":", estado)


# ----------------------------------------
# Procedimiento para mantenimiento preventivo
# ----------------------------------------
def mantenimiento_preventivo():

    print("\nPlanificando mantenimiento")

    for maquina, estado in maquinas.items():

        if estado == "detenida":
            print("Se programa mantenimiento para", maquina)

        elif estado == "mantenimiento":
            print(maquina, "ya está en mantenimiento")

        else:
            print(maquina, "funciona correctamente")


# ----------------------------------------
# Función para analizar rendimiento
# ----------------------------------------
def analizar_rendimiento():

    produccion = random.randint(50, 150)
    produccion_diaria.append(produccion)

    promedio = sum(produccion_diaria) / len(produccion_diaria)

    print("\nProducción del día:", produccion)
    print("Promedio de producción:", round(promedio, 2))


# ----------------------------------------
# Procedimiento para ajustar producción
# ----------------------------------------
def ajustar_produccion():

    demanda = random.choice(["baja", "media", "alta"])

    print("\nDemanda del mercado:", demanda)

    if demanda == "alta":
        print("Aumentar turnos de producción")

    elif demanda == "media":
        print("Mantener producción actual")

    else:
        print("Reducir producción para evitar exceso")


# ----------------------------------------
# Menú principal
# ----------------------------------------
def menu():

    while True:

        print("\n===== SISTEMA PRODUCCIÓN FÁBRICA =====")
        print("1 Monitorear máquinas")
        print("2 Planificar mantenimiento")
        print("3 Analizar rendimiento")
        print("4 Ajustar producción")
        print("0 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monitorear_maquinas()

        elif opcion == "2":
            mantenimiento_preventivo()

        elif opcion == "3":
            analizar_rendimiento()

        elif opcion == "4":
            ajustar_produccion()

        elif opcion == "0":
            print("Sistema finalizado")
            break

        else:
            print("Opción inválida")


menu()