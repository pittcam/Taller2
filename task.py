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
