
from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    print("---- Ordem Crescente (Pior Caso)")
    heap_crescente = BinaryHeap()
    for val in [10, 20, 30, 40, 50]:
        heap_crescente.insert(val)
    print(f"Estado: {heap_crescente.data} | Total de Trocas: {heap_crescente.swap_count}")

    print("\n--- Ordem Decrescente (Melhor Caso)")
    heap_decrescente = BinaryHeap()
    for val in [50, 40, 30, 20, 10]:
        heap_decrescente.insert(val)
    print(f"Estado: {heap_decrescente.data} | Total de Trocas: {heap_decrescente.swap_count}")

    print("\n--- Ordem Aleatória")
    heap_aleatoria = BinaryHeap()
    for val in [15, 50, 10, 40, 30]:
        heap_aleatoria.insert(val)
    print(f"Estado: {heap_aleatoria.data} | Total de Trocas: {heap_aleatoria.swap_count}")
    