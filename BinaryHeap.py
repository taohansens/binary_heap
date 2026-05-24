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

    def extract_max(self):
        if not self.data:
            return None

        # Se tiver apenas 1 elem. não precisa reorganizar.
        if len(self.data) == 1:
            return self.data.pop()

        # Pega o valor máximo (raiz) para retornar no final
        max_val = self.data[0]

        # Move o último elemento da lista para a raiz e o remove do final
        # preserva a invariante de forma da árvore quase completa
        self.data[0] = self.data.pop()

        # Reorganiza a árvore de cima para baixo para preservar a invariante de ordem
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

        # Verifica se o filho da direita existe e é maior que o maior até agora
        if right < size and self.data[right] > self.data[largest]:
            largest = right

        # Se o maior não for o nó atual, realiza a troca e desce
        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self.swap_count += 1
            self._sift_down(largest)

    def contains(self, valor):
        for item in self.data:
            if item == valor:
                return True
        return False

    def delete(self, valor):
        try:
            index = self.data.index(valor)
        except ValueError:
            return False

        if index == len(self.data) - 1:
            self.data.pop()
            return True

        # Substitui o elemento a ser removido pelo último
        self.data[index] = self.data.pop()

        # Reorganiza a heap a partir do índice modificado
        # O elemento trocado pode precisar subir ou descer
        parent_idx = self.parent(index)

        # Se não é a raiz e é maior que o pai, ele deve subir
        if index > 0 and self.data[index] > self.data[parent_idx]:
            self._sift_up(index)
        else:
            # Se não, descer
            self._sift_down(index)

        return True

    def is_valid_heap(self, array):
        n = len(array)

        # Percorre apenas os nós que possuem filhos (até a metade)
        for i in range((n - 2) // 2 + 1):
            left = 2 * i + 1
            right = 2 * i + 2

            # Verifica se o filho da esquerda existe e se viola a regra da Max-Heap
            if left < n and array[left] > array[i]:
                return False

            # Verifica se o filho da direita existe e se viola a regra da Max-Heap
            if right < n and array[right] > array[i]:
                return False

        return True