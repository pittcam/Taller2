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
