# Algoritmo MaxMin Select

Uma implementação em Python do algoritmo de divisão e conquista para encontrar o valor máximo e mínimo em um array.

## Algoritmo

### Funcionamento (Linha por Linha)

1. **max_min_select(arr, left, right)**
   ```python
   def max_min_select(arr, left, right):
       # Caso base: um elemento
       if left == right:
           return arr[left], arr[left]
       
       # Caso base: dois elementos
       if right - left == 1:
           if arr[left] > arr[right]:
               return arr[left], arr[right]
           return arr[right], arr[left]

       # Divisão
       mid = (left + right) // 2
       
       # Conquista: chamadas recursivas
       max1, min1 = max_min_select(arr, left, mid)
       max2, min2 = max_min_select(arr, mid + 1, right)
       
       # Combinação
       return max(max1, max2), min(min1, min2)
   ```

   - Divide o array em duas metades
   - Recursivamente encontra máximo e mínimo em cada metade
   - Combina os resultados usando max() e min()

## Executando o Projeto

1. Clone o repositório
   ```bash
   git clone https://github.com/AnaCarolinaMello/fpaa-trabalho-2
   ```
2. Certifique-se de que o Python 3.x está instalado
3. Execute o programa:
   ```bash
   python main.py
   ```
   ou
   ```bash
   python3 main.py
   ```
   ou
   ```bash
   py main.py
   ```
4. Digite um número ou r para ver o resultado

## Relatório Técnico

### Análise de Complexidade por Contagem de Operações

O algoritmo pode ser analisado em três partes principais:

1. **Divisão**
   - Cálculo do ponto médio: O(1)

2. **Recursão**
   - Duas chamadas recursivas com tamanho n/2

3. **Combinação**
   - Duas comparações (max e min): O(1)

Total de comparações para n elementos:
- T(n) = 2T(n/2) + O(1)

### Análise pelo Teorema Mestre

Para a recorrência T(n) = 2T(n/2) + O(1):

1. **Parâmetros**
   - a = 2 (número de subproblemas)
   - b = 2 (fator de divisão)
   - f(n) = O(1) (custo da combinação)

2. **Cálculo de logₐb**
   - log₂2 = 1

3. **Aplicação do Teorema Mestre**
   - f(n) = O(1)
   - n^(log₂2) = n
   - Como 1 = O(n^0), estamos no caso 2
   - Portanto, T(n) = O(n)

### Complexidade Final

- **Tempo**: O(n)
- **Espaço**: O(log n) devido à pilha de recursão

### Vantagens

1. Eficiente para grandes conjuntos de dados
2. Número ótimo de comparações
3. Facilmente paralelizável

### Referências

1. Cormen, T. H., et al. "Introduction to Algorithms"
2. Horowitz, E. and Sahni, S. "Fundamentals of Computer Algorithms"
