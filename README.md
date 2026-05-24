# Implementação de Max-Heap Binária em Python

## Sobre o Projeto
Este projeto consiste na implementação de uma estrutura de dados **Max-Heap Binária** do zero, desenvolvida em Python. O objetivo principal é consolidar conceitos de estruturas de dados, complexidade algorítmica e Programação Orientada a Objetos (OO). A estrutura foi projetada para resolver problemas de priorização dinâmica, como o escalonamento de processos em um Sistema Operacional.

## Arquitetura e Invariantes
A arquitetura da classe `BinaryHeap` foi construída para ser testável, modular e extensível:
* **Armazenamento:** O estado interno utiliza exclusivamente uma lista (`array`) nativa do Python, sem o uso de ponteiros.
* **Invariante de Forma:** A árvore estrutural é mantida como "quase completa" (preenchida da esquerda para a direita), permitindo o mapeamento contíguo na memória.
* **Invariante de Ordem:** A propriedade de Max-Heap garante que qualquer nó pai seja maior ou igual aos seus filhos, mantendo o elemento de maior prioridade sempre no índice 0 ($O(1)$).

## Funcionalidades e Complexidade (Big O)
O projeto implementa as seguintes operações principais:
* **Inserção (`insert`) e *sift-up*:** Adiciona um novo elemento mantendo as invariantes. Complexidade: **$O(\log n)$**.
* **Remoção da Raiz (`extract_max`) e *sift-down*:** Extrai o elemento de maior prioridade (raiz). Complexidade: **$O(\log n)$**.
* **Busca Linear (`contains`):** Verifica a existência de um valor. Devido à ordenação ser estritamente vertical, exige varredura. Complexidade: **$O(n)$**.
* **Remoção Arbitrária (`delete`):** Remove um elemento em qualquer posição e reorganiza a heap. Complexidade: **$O(n)$**.
* **Construção Otimizada (`build_heap`):** Utiliza o método de Floyd para construir a heap em lote a partir de um array desordenado. Complexidade: **$O(n)$**.
* **Validação Estrutural (`is_valid_heap`):** Função independente que verifica se um array bruto respeita as propriedades lógicas da heap. Complexidade: **$O(n)$**.
* **Heap Sort Parcial (`get_k_largest`):** Extrai os *k* maiores elementos de um array sem ordená-lo completamente. Complexidade: **$O(n + k \log n)$**.

## Análise Empírica
O código foi instrumentado de forma a contabilizar trocas em memória desde o início (`swap_count`) ao longo das execuções. Os testes práticos confirmaram a precisão da análise teórica:
* **Construção incremental (`insert` sucessivo):** Apresentou crescimento log-linear acelerado **$O(n \log n)$**.
* **Construção em lote (`build_heap`):** Demonstrou uma economia de quase 50% de operações para arrays de grande escala (ex: 1 milhão de itens), validando empiricamente a eficiência da complexidade linear **$O(n)$**.