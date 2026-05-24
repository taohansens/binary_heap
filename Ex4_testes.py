from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()
    for val in [50, 40, 30, 20, 10, 5]:
        heap.insert(val)

    print(f"Heap Inicial: {heap.data}\n")

    print("Iniciando Remoção")
    passo = 1

    while heap.data:
        removido = heap.extract_max()
        print(f"Passo {passo} | Removido: {removido:02d} | Novo estado da Heap: {heap.data}")
        passo += 1

    print("\nHeap vazia!")
