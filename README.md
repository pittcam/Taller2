# Taller 2

Este taller tiene como objetivo desarrollar una función eficiente en Python que encuentre pares de enteros en una lista cuya suma sea igual a un valor dado. La función tomará como entrada la lista de números y la suma objetivo, devolviendo los pares encontrados.

## Integrantes:
- Maikol Vergara
- Juan Perez
- Juan Barajas
- Juliana Castro
- Valentina León
- Lukas Rodríguez

## Descripción del Problema
Se proporciona un ejecutable llamado "app" que acepta una lista de enteros separados por comas y el entero de destino como argumentos de línea de comandos. La tarea consiste en implementar una función que realice la búsqueda de pares dentro de la lista, garantizando que:

- Son implementados tres algoritmos de complejidad exponencial (O(n^2)), lineal (O(n)) y logarítmica (O(log(n)), mostrando después mediante análisis empírico cuál es más eficiente.
- La entrada se asume como una lista de enteros sin repeticiones.
- La implementación debe ser eficiente y devolver resultados correctos para todas las entradas posibles.

## Requisitos Adicionales
- No se requiere la implementación de mecanismos de entrada/salida idénticos a los de la aplicación de ejemplo.
- No se requieren pruebas unitarias.

## Resultados
El proceso implica la generación de gráficas que ilustren el tiempo de ejecución de cada algoritmo en relación con el tamaño de la lista de entrada (n). Se planea utilizar conjuntos de datos de diversos tamaños con el objetivo de evaluar cómo cada algoritmo se desempeña y escala con n.

![grafica2](https://github.com/pittcam/Taller2/assets/140974091/c0bd65c2-5f22-4163-8eef-53c9c95e49fd)
![grafica1](https://github.com/pittcam/Taller2/assets/140974091/573b7f06-94e9-4be2-aa59-45001f34baef)
![grafica3](https://github.com/pittcam/Taller2/assets/140974091/6aa3fcb5-a048-4343-97cc-3284d71a2727)


El código implementa tres funciones diferentes (encontrar_pares_lineal, encontrar_pares_exponencial, y encontrar_pares_logn) para encontrar pares de números en un arreglo que suman un objetivo dado. Además, el programa permite generar un arreglo aleatorio, mostrarlo, y luego ejecutar cada función para encontrar los pares. También ofrece una opción para comparar los tiempos de ejecución acumulados de estas funciones y graficarlos.

Vamos a realizar un análisis de complejidad para cada una de las funciones:

- Función encontrar_pares_lineal:
### Complejidad: O(n)
Análisis: Utiliza un conjunto (visto) para realizar la búsqueda de manera lineal en el arreglo. El tiempo de ejecución depende del tamaño del arreglo (n), y en el peor caso, puede recorrer todo el arreglo una vez.

- Función encontrar_pares_exponencial:
### Complejidad: O(n^2)
Análisis: Utiliza dos bucles anidados para comparar todas las combinaciones posibles de elementos en el arreglo. La complejidad cuadrática implica un tiempo de ejecución que escala cuadráticamente con el tamaño del arreglo (n). 

-Función encontrar_pares_logn:
### Complejidad: O(n log n)
La función utiliza la técnica de búsqueda binaria después de ordenar el arreglo. El tiempo de ejecución se ve dominado por el costo de la clasificación, que es O(n log n) en el peor caso. 

En base al análisis de complejidad y la gráficas, que analiza el comportamiento de los tres algoritmos con un tamaño de arreglo de más de 300, 2500 y 4000 números. El algoritmo más eficiente es el de complejidad O(log(n), es decir, la función encontrar_pares_logn. Esta función tiene un rendimiento constante y tiende a ser más eficiente en términos de tiempo de ejecución para conjuntos de datos más grandes en comparación con las otras dos funciones. Luego, sigue el algoritmo lineal y por último y más ineficiente, el exponencial, que toma el doble de tiempo en ejecutarse que los otros dos.



