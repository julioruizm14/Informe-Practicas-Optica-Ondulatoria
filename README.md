# Prácticas de Laboratorio - Óptica Ondulatoria 

Este repositorio alberga la memoria de prácticas y el código de análisis correspondiente a la asignatura de **Óptica II** del Grado en Física (Curso 2020/2021).

El proyecto se centra en el estudio experimental de la naturaleza ondulatoria de la luz, abarcando fenómenos de polarización, interferencias y difracción, contrastando los resultados experimentales con modelos teóricos mediante scripts en **Python**.

## Contenido del Repositorio

* **`Informe_practicas_optica_ondulatoria.pdf`**: Memoria completa que documenta cuatro bloques de prácticas, incluyendo introducción teórica, montaje experimental, fotografías y conclusiones.
* **`CodigoP1.py`**: Script en Python utilizado para el análisis de la **Práctica I** (Polarización), graficando las ecuaciones de Fresnel y la Ley de Malus.

---

## Experimentos Realizados

### 0. Fotografía de Fenómenos Ópticos
Visualización cualitativa de principios ópticos básicos mediante experimentos caseros.
* **Ley de Snell:** Visualización de la refracción láser en medios con índices constantes y gradientes de índice (azúcar disuelta).
* **Dispersión de Rayleigh:** Simulación de una atmósfera terrestre usando una emulsión de agua y leche para observar el cambio de color de la luz (dispersión de longitudes de onda cortas).

### 1. Polarización y Ecuaciones de Fresnel
Estudio cuantitativo del comportamiento vectorial de la luz.
* **Ecuaciones de Fresnel:** Medición de la intensidad reflejada en un prisma para polarizaciones paralela y perpendicular.
    * **Resultado:** Cálculo del ángulo de Brewster ($\theta_B \approx 51.5^\circ$) y determinación del índice de refracción del vidrio ($n \approx 1.257$).
* **Ley de Malus:** Verificación de la variación de intensidad ($I = I_0 \cos^2\theta$) al rotar dos polarizadores lineales.
* **Birrefringencia:** Observación cualitativa mediante materiales plásticos bajo tensión.
* **Parámetros de Stokes:** Determinación experimental del vector de Stokes para luz lineal y circular.

### 2. Interferencias
Análisis de la superposición de ondas luminosas coherentes.
* **Doble Rendija de Young:** Medición del patrón de interferencias para determinar la longitud de onda del láser.
    * **Resultado:** $\lambda = 600 \pm 49 \text{ nm}$.
    * Cálculo de la separación entre rendijas: $d \approx 0.171 \text{ mm}$.
* **Interferómetro de Michelson:** Calibración del instrumento y observación de anillos de interferencia, notando su alta sensibilidad a vibraciones micrométricas.

### 3. Difracción
Estudio de la desviación de la luz al encontrar obstáculos.
* **Difracción de Fraunhofer:** Análisis de rendija simple y comparación con la doble rendija (efecto de envolvente).
* **Red de Difracción:** Determinación de la densidad de líneas de la red.
    * **Resultado:** $\approx 535.8 \text{ franjas/mm}$.
* **Espectroscopía:** Uso de la red de difracción para descomponer la luz de una lámpara de descarga y medir las longitudes de onda de las líneas espectrales.
    * **Conclusión:** Identificación del elemento emisor como **Cadmio (Cd)** comparando con su espectro teórico.

---

## Requisitos y Ejecución del Código

El análisis de datos de la Práctica I se realizó en **Python**. El script `CodigoP1.py` genera las gráficas comparativas entre los datos experimentales y las curvas teóricas.

### Librerías necesarias:
```python
pip install numpy matplotlib
```

Funcionalidad del script:
- Fresnel: Grafica la intensidad reflejada frente al ángulo de incidencia para polarizaciones paralela y perpendicular, ajustando los datos experimentales a las ecuaciones teóricas.
- Malus: Representa la caída de intensidad de la luz al cruzar polarizadores, incluyendo correcciones por desplazamiento angular.
