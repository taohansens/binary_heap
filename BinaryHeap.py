class BinaryHeap:
    def __init__(self):
        self.data = []
        self.swap_count = 0

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, valor):
        # 1. Adiciona o elemento ao final
        self.data.append(valor)
        # 2. Reorganiza para cima
        self._sift_up(len(self.data) - 1)

    def _sift_up(self, index):
        # Enquanto não for a raiz e o pai for menor que o nó atual (violação da Max-Heap)
        while index > 0 and self.data[self.parent(index)] < self.data[index]:
            # Troca o nó atual com o pai
            pai_idx = self.parent(index)
            self.data[pai_idx], self.data[index] = self.data[index], self.data[pai_idx]

            # Registra a troca
            self.swap_count += 1

            # Muda o índice para continuar subindo
            index = pai_idx

    def extract_max(self):
        if not self.data:
            return None  # Heap vazia
        if len(self.data) == 1:
            return self.data.pop()  # Apenas um elemento

        # O maior elemento é sempre a raiz (índice 0)
        max_val = self.data[0]

        # Move o último elemento da lista para a raiz e remove o último nó
        self.data[0] = self.data.pop()

        # Reorganiza a árvore de cima para baixo
        self._sift_down(0)

        return max_val

    def _sift_down(self, index):
        size = len(self.data)
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)

        # Verifica se o filho da esquerda existe e é maior que o nó atual
        if left < size and self.data[left] > self.data[largest]:
            largest = left

        # Verifica se o filho da direita existe e é maior que o valor mais alto até agora
        if right < size and self.data[right] > self.data[largest]:
            largest = right

        # Se o maior não for o nó atual, troca e continua descendo
        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self.swap_count += 1
            self._sift_down(largest)