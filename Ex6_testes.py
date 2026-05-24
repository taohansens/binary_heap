from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()
    for val in [50, 40, 30, 20, 10, 5]:
        heap.insert(val)

    print(f"Heap Inicial: {heap.data}\n")

    print("\n--- Removendo valor existente (30) ---")
    sucesso = heap.delete(30)
    print(f"Sucesso: {sucesso} | Novo estado: {heap.data}")

    print("\n--- Removendo a raiz (50) ---")
    sucesso = heap.delete(50)
    print(f"Sucesso: {sucesso} | Novo estado: {heap.data}")

    print("\n--- Removendo valor inexistente (99) ---")
    sucesso = heap.delete(99)
    print(f"Sucesso: {sucesso} | Novo estado: {heap.data}")