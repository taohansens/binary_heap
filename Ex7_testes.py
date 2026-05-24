from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()

    print("Validação de Heap ")
    array_valido = [50, 40, 30, 20, 10, 5]
    print(f"Array: {array_valido} | É uma Heap Válida? {heap.is_valid_heap(array_valido)}")

    array_invalido = [50, 40, 60, 20, 10, 5]
    print(f"Array: {array_invalido} | É uma Heap Válida? {heap.is_valid_heap(array_invalido)}")

    array_invalido_2 = [50, 20, 30, 25, 10, 5]
    print(f"Array: {array_invalido_2} | É uma Heap Válida? {heap.is_valid_heap(array_invalido_2)}")
    