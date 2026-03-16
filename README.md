# Sistemas Inteligentes con Programación Modular en Python

Este repositorio contiene la implementación de cinco sistemas que resuelven problemas reales mediante el uso de **programación modular utilizando funciones y procedimientos en Python**.

Cada sistema está diseñado para dividir el problema en partes más pequeñas mediante funciones reutilizables, lo que mejora la organización, mantenimiento y eficiencia del código.

---

# 1. Control de Temperatura en un Edificio Inteligente

Este sistema simula el control de temperatura en diferentes zonas de un edificio inteligente con el objetivo de **optimizar el consumo de energía**.

El sistema considera:

- Hora del día
- Ocupación de las zonas
- Condiciones climáticas externas

Funciones implementadas:

- **leer_sensores()**  
  Lee los datos de sensores de temperatura.

- **calcular_temperatura_optima()**  
  Calcula la temperatura ideal para cada zona.

- **ajustar_sistema()**  
  Envía señales al sistema de calefacción o refrigeración.

- **registrar_consumo_energia()**  
  Registra el consumo energético del sistema.

---

# 2. Gestión de Inventario en un Almacén

Este sistema permite controlar el inventario de productos dentro de un almacén, registrando las entradas y salidas de mercancía.

Objetivos del sistema:

- Evitar falta de productos
- Reducir exceso de inventario
- Optimizar el reabastecimiento

Funciones implementadas:

- **registrar_entrada()**  
  Agrega productos al inventario.

- **registrar_salida()**  
  Registra la salida de productos del almacén.

- **calcular_inventario_optimo()**  
  Determina si el inventario es adecuado, bajo o excesivo.

- **alerta_reabastecimiento()**  
  Genera alertas cuando el inventario es bajo.

- **mostrar_inventario()**  
  Muestra todos los productos y su cantidad disponible.

---

# 3. Sistema de Navegación para un Vehículo Autónomo

Este sistema simula la navegación de un vehículo autónomo que planifica rutas, detecta obstáculos y ajusta la velocidad según el tráfico.

Funciones implementadas:

- **leer_sensores()**  
  Lee datos de sensores de proximidad.

- **calcular_ruta()**  
  Determina la ruta óptima para el vehículo.

- **evitar_obstaculos()**  
  Detecta obstáculos y realiza maniobras de evasión.

- **ajustar_velocidad()**  
  Ajusta la velocidad según las condiciones del tráfico.

---

# 4. Optimización de la Producción en una Fábrica

Este sistema permite mejorar la eficiencia de producción en una fábrica mediante el monitoreo de máquinas y la planificación de mantenimiento.

Funciones implementadas:

- **monitorear_maquinas()**  
  Verifica el estado de las máquinas.

- **mantenimiento_preventivo()**  
  Planifica mantenimiento cuando es necesario.

- **analizar_rendimiento()**  
  Analiza la producción diaria.

- **ajustar_produccion()**  
  Ajusta la producción según la demanda del mercado.

---

# 5. Sistema de Riego Automatizado para Agricultura

Este sistema optimiza el uso del agua en la agricultura considerando la humedad del suelo y las condiciones climáticas.

Funciones implementadas:

- **leer_humedad()**  
  Lee los sensores de humedad del suelo.

- **consultar_clima()**  
  Consulta la previsión meteorológica.

- **calcular_riego()**  
  Determina la cantidad óptima de riego.

- **controlar_valvulas()**  
  Controla las válvulas de riego en diferentes secciones del campo.

---

# Beneficios de la Programación Modular

El uso de funciones y procedimientos permite:

- Mejor organización del código
- Mayor reutilización de funciones
- Mayor facilidad para mantenimiento
- Mejor rendimiento del sistema

---

# Estructura del Proyecto
