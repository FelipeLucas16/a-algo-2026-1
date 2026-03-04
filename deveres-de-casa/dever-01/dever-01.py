import random
import time

# Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = chave


# Tamanhos das listas
tamanhos = [1000, 5000, 10000, 20000, 50000]

print("Comparação de tempo: Insertion Sort vs sorted()")
print("-" * 50)

for n in tamanhos:
    # Gera lista aleatória
    lista = [random.randint(0, 100000) for _ in range(n)]
    
    # Cópia da lista para não ordenar a mesma
    lista_insertion = lista.copy()
    lista_sorted = lista.copy()

    # Medir tempo do Insertion Sort
    inicio = time.perf_counter()
    insertion_sort(lista_insertion)
    fim = time.perf_counter()
    tempo_insertion = fim - inicio
    
    # Medir tempo do sorted()
    inicio = time.perf_counter()
    sorted(lista_sorted)
    fim = time.perf_counter()
    tempo_sorted = fim - inicio
    
    # Mostrar resultados
    print(f"n = {n}")
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"sorted()      : {tempo_sorted:.6f} segundos")
    print("-" * 50)