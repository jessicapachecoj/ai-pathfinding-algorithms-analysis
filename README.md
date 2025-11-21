# 🗺️ AI-Pathfinding-Algorithms-Analysis

**Foco:** Implementação e análise comparativa dos principais algoritmos de busca em grafos (**A\***, **BFS** e **DFS**) aplicados à simulação de rotas rodoviárias entre as capitais brasileiras. Demonstra proficiência em algoritmos de otimização e estruturas de dados.

---

## 1. 📖 Contexto e Propósito do Projeto

Este projeto resolve o desafio de encontrar o **caminho mais eficiente** entre dois pontos em um grafo complexo, simulando a rede viária do Brasil. O objetivo é **comparar a performance, a distância percorrida e o esforço computacional** (operações) de três métodos de busca distintos.

O trabalho comprova o domínio sobre:

- **Estruturas de Dados:** Uso de Grafos (para o mapa), Filas (para BFS), Pilhas (para DFS) e Filas de Prioridade (para A\*).
- **Inteligência Artificial:** Aplicação e ajuste de heurísticas (Busca A\*) para guiar a busca e otimizar o resultado.
- **Análise de Performance:** Quantificação e comparação da eficiência algorítmica entre métodos cegos (BFS/DFS) e informados (A\*).

---

## 2. 🏗️ Arquitetura e Componentes Chave

O sistema é construído em **Python** e opera sobre um grafo pré-definido.

### 🇧🇷 Grafo de Conexões (Mapa do Brasil)
- O mapa é representado por um **dicionário**, onde as chaves são as capitais e os valores são dicionários com **vizinhos** e as **distâncias rodoviárias** entre eles (arestas ponderadas).
- Inclui as **coordenadas geográficas** (latitude e longitude) de cada capital, essenciais para o cálculo da **heurística A\***.

### 🧠 Algoritmos de Busca
- **Busca em Largura (BFS):** Garante a menor quantidade de passos, sendo ótimo em grafos com pesos uniformes. Utiliza `deque` (Fila).  
- **Busca em Profundidade (DFS):** Prioriza a profundidade da busca. Implementado de forma iterativa utilizando Pilha.  
- **Algoritmo A\*:** Busca informada que usa uma **função heurística** para determinar o caminho de menor custo total. Utiliza `heapq` (Fila de Prioridade).

---

## 3. 🎯 Estratégias e Heurísticas

O diferencial do projeto está na **implementação e avaliação da heurística**:

### Heurística Utilizada
- A heurística para o Algoritmo **A\*** é a **Distância em Linha Reta** (ou **Haversine Distance**), calculada a partir das coordenadas geográficas.
- **Cálculo:** A função `distancia_entre_cidades` usa a fórmula de Haversine para estimar a distância real mais próxima em linha reta (**h(n)**), garantindo que a heurística seja **admissível** (nunca superestima o custo real).

### Função de Avaliação (A\*)
- **f(n) = g(n) + h(n)**
  - **g(n):** Custo real do caminho percorrido (distância rodoviária).  
  - **h(n):** Custo estimado até o destino (distância em linha reta).

---

## 4. 📊 Resultados e Análise Comparativa

O programa gera saídas que facilitam a **comparação técnica**:

- **Saídas por Método:** Exibe o caminho completo, a distância total percorrida e o número de operações (cidades visitadas/expandidas).
- **Tabela de Comparação:** Apresenta um resumo lado a lado para avaliar:
  - **Otimização de Custo:** A\* é mais eficiente em encontrar o caminho de menor distância rodoviária.
  - **Eficiência Temporal:** Comparativo do número de operações entre os três métodos.
  - **Completude:** Verifica se o caminho pode ser alcançado, mesmo com a busca cega (BFS/DFS).

---

## 5. 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python (foco em legibilidade e eficiência algorítmica).  
- **Bibliotecas:**  
  - `heapq` → Fila de Prioridade do A\*  
  - `collections.deque` → Fila do BFS  
  - `math` → Função Haversine  
- **Conceitos de IA:** Grafos, Heurísticas Admissíveis, Algoritmos de Busca.
