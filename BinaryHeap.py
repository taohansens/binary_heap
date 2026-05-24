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