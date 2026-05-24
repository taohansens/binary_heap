from BinaryHeap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()
    dados = [15, 3, 9, 21, 14, 50, 2, 7, 33]

    print(f"Os 3 maiores: {heap.get_k_largest(dados, 3)}")
    print(f"Os 5 maiores: {heap.get_k_largest(dados, 5)}")