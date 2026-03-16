# Sistemas Inteligentes con Programación Modular

Este repositorio contiene la implementación de dos sistemas desarrollados utilizando programación modular mediante funciones y procedimientos en Python.

Los programas están diseñados para resolver problemas reales utilizando funciones reutilizables que mejoran la organización, mantenimiento y rendimiento del código.

---

# 1. Control de Temperatura en un Edificio Inteligente

Este sistema simula el control de temperatura en un edificio inteligente con el objetivo de optimizar el consumo de energía.

El sistema ajusta la temperatura dependiendo de:

- Hora del día
- Ocupación de las zonas
- Condiciones climáticas externas

## Funciones implementadas

### leer_sensores()
Lee los datos de los sensores de temperatura en diferentes zonas del edificio.

### calcular_temperatura_optima()
Calcula la temperatura ideal para cada zona considerando la hora del día, la ocupación y el clima.

### ajustar_sistema()
Envía señales al sistema de calefacción o refrigeración para ajustar la temperatura.

### registrar_consumo_energia()
Registra y analiza el consumo energético del sistema de climatización.

### Beneficio de la modularidad

La separación en funciones permite reutilizar cada componente del sistema, facilitando el mantenimiento del código y mejorando el rendimiento del sistema.

---

# 2. Gestión de Inventario en un Almacén

Este sistema permite administrar el inventario de productos dentro de un almacén registrando entradas, salidas y controlando el nivel de stock.

El objetivo es evitar:

- falta de productos
- exceso de inventario
- problemas de abastecimiento

## Funciones implementadas

### registrar_entrada()
Permite agregar productos al inventario cuando llegan al almacén.

### registrar_salida()
Registra la salida de productos cuando se venden o distribuyen.

### calcular_inventario_optimo()
Analiza la cantidad de productos en el inventario y determina si el stock es adecuado, bajo o excesivo.

### alerta_reabastecimiento()
Genera alertas cuando un producto tiene un nivel bajo de inventario y necesita ser reabastecido.

### mostrar_inventario()
Muestra todos los productos almacenados y su cantidad disponible.

### Beneficio de la modularidad

El uso de funciones permite que cada operación del inventario sea independiente, lo que facilita la escalabilidad del sistema y mejora la eficiencia en el manejo de datos.

---

# Estructura del Proyecto
