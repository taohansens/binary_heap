from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    array_base = [i for i in range(1, 101)] # pior caso para inserção (ordenado)

    # 9.1 (inserção incremental)
    heap_incremental = BinaryHeap()
    for val in array_base:
        heap_incremental.insert(val)
    print(f"Trocas na Inserção Incremental: {heap_incremental.swap_count}")

    # 9.2 (usando o build_heap)
    heap_build = BinaryHeap()
    heap_build.build_heap(array_base)
    print(f"Trocas com build_heap: {heap_build.swap_count}")
