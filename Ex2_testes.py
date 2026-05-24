from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()

    valores_para_inserir = [95,60,78,39,28,66,70,33]

    for valor in valores_para_inserir:
        heap.insert(valor)
        print(f"Inserido: {valor:02d} | Estado interno da Heap (lista): {heap.data}")

    print(f"Total de trocas (sift-ups) realizadas: {heap.swap_count}")

    print("\n--- Testando a Remoção (Extract-Max) ---")
    # Removendo sucessivamente até esvaziar
    while heap.data:
        removido = heap.extract_max()
        print(f"Removido: {removido:02d} | Estado interno da Heap (lista): {heap.data}")