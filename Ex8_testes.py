from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()

    array_pequeno = [3, 1, 6, 5, 2, 4]
    heap.build_heap(array_pequeno)
    print(f"Array Pequeno: {heap.data}")

    array_maior = [10, 20, 15, 30, 40, 50, 60, 5, 1, 9]
    heap.build_heap(array_maior)
    print(f"Array Maior: {heap.data}")
    