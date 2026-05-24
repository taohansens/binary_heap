from BinaryHeap import BinaryHeap
import random

if __name__ == "__main__":
    tamanhos = [100, 1000, 10000,100000,1000000]

    print(f"{'Tamanho (N)':<15} | {'Build-Heap O(N)':<20} | {'Insert O(N log N)':<20}")
    print("-" * 60)

    for n in tamanhos:
        dados = [random.randint(1, 1000000) for _ in range(n)]

        # Teste O(N log N)
        h_inc = BinaryHeap()
        for v in dados:
            h_inc.insert(v)

        # Teste O(N)
        h_bld = BinaryHeap()
        h_bld.build_heap(dados)

        print(f"{n:<15} | {h_bld.swap_count:<20} | {h_inc.swap_count:<20}")
        