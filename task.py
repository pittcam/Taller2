import random
import time
import matplotlib.pyplot as plt

def generar_arreglo(tamaño):
    return [random.randint(0, 30) for _ in range(tamaño)]

def encontrar_pares_lineal(arreglo, objetivo):
    visto = set()
    pares = []
    tiempos = []
    start_time = time.time()

    for num in arreglo:
        complemento = objetivo - num
        if complemento in visto:
            pares.append((complemento, num))
            tiempos.append(time.time() - start_time)
        visto.add(num)

    return pares, tiempos

def encontrar_pares_exponencial(arreglo, objetivo):
    pares = []
    tiempos = []
    start_time = time.time()

    for i in range(len(arreglo)):
        for j in range(i + 1, len(arreglo)):
            if arreglo[i] + arreglo[j] == objetivo:
                pares.append((arreglo[i], arreglo[j]))
                tiempos.append(time.time() - start_time)

    return pares, tiempos
def encontrar_pares_logn(arreglo, objetivo):
    arreglo.sort()
    izquierda, derecha = 0, len(arreglo) - 1
    pares = []
    tiempos = []
    start_time = time.time()

    while izquierda < derecha:
        suma_actual = arreglo[izquierda] + arreglo[derecha]

        if suma_actual == objetivo:
            pares.append((arreglo[izquierda], arreglo[derecha]))
            tiempos.append(time.time() - start_time)
            izquierda += 1
            derecha -= 1
        elif suma_actual < objetivo:
            izquierda += 1
        else:
            derecha -= 1

    return pares, tiempos

def graficar_tiempos_acumulados(tiempos, nombres):
  plt.figure(figsize=(10, 6))
  for i, tiempos_funcion in enumerate(tiempos):
      plt.plot(tiempos_funcion, label=nombres[i])
  plt.title('Comparación de Tiempo Acumulado de Ejecución')
  plt.xlabel('Número de Pares Encontrados')
  plt.ylabel('Tiempo Acumulado (segundos)')
  plt.legend()
  plt.show()
def menu():
  tamaño = int(input("Ingrese el tamaño del arreglo: "))
  objetivo = int(input("Ingrese el número objetivo para la suma de pares: "))
  arreglo = generar_arreglo(tamaño)

  while True:
      print("\nMenú:")
      print("1. Mostrar el arreglo generado")
      print("2. Mostrar pares usando la función Lineal")
      print("3. Mostrar pares usando la función Exponencial")
      print("4. Mostrar pares usando la función O(log n)")
      print("5. Comparar tiempos de ejecución y graficar")
      print("6. Salir")
      eleccion = input("Seleccione una opción: ")

      if eleccion == '1':
          print("Arreglo:", arreglo)
      elif eleccion == '2':
          pares, tiempo = encontrar_pares_lineal(arreglo, objetivo)
          print("Pares encontrados (Lineal):", pares)
          print("Tiempo de ejecución (Lineal):", tiempo, "segundos")
      elif eleccion == '3':
          pares, tiempo = encontrar_pares_exponencial(arreglo, objetivo)
          print("Pares encontrados (Exponencial):", pares)
          print("Tiempo de ejecución (Exponencial):", tiempo, "segundos")
      elif eleccion == '4':
          pares, tiempo = encontrar_pares_logn(arreglo, objetivo)
          print("Pares encontrados (O(log n)):", pares)
          print("Tiempo de ejecución (O(log n)):", tiempo, "segundos")
      if eleccion == '5':  # Opción de comparación de tiempos
        pares_lineal, tiempos_lineal = encontrar_pares_lineal(arreglo, objetivo)
        pares_exponencial, tiempos_exponencial = encontrar_pares_exponencial(arreglo, objetivo)
        pares_logn, tiempos_logn = encontrar_pares_logn(arreglo, objetivo)
