class BinaryHeap:
    def __init__(self):
        self.data = []
        self.swap_count = 0

    # Índices de pai e filhos
    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        # Idx filho à esquerda.
        return 2 * index + 1

    def right_child(self, index):
        # Idx filho à direita
        return 2 * index + 2

    def insert(self, valor):
        # Adiciona ao final da lista (invariante de forma)
        self.data.append(valor)
        # Inicia o processo de reorganização a partir do último índice add
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, index):
        # Enquanto não chegar à raiz e o pai for menor que o nó atual (violando a Max-Heap)
        while index > 0 and self.data[self.parent(index)] < self.data[index]:
            pai_idx = self.parent(index)

            # Realiza a troca entre o nó atual e o pai
            self.data[pai_idx], self.data[index] = self.data[index], self.data[pai_idx]

            # +1 na qtd de troca
            self.swap_count += 1

            # Atualiza o índice para o do pai e continua o laço
            index = pai_idx
