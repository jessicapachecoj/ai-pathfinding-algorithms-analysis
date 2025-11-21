import heapq
import math
from collections import deque
from unicodedata import normalize

conexoes_capitais = {
    'Rio Branco': {'Porto Velho': 544, 'Manaus': 1445},  
    'Porto Velho': {'Rio Branco': 544, 'Manaus': 901, 'Cuiabá': 1456},
    'Manaus': {'Porto Velho': 901, 'Boa Vista': 785, 'Belém': 5298, 'Rio Branco': 1445},
    'Boa Vista': {'Manaus': 785},
    'Belém': {'Manaus': 5298, 'São Luís': 806, 'Palmas': 1269, 'Macapá': 308},
    'São Luís': {'Belém': 806, 'Teresina': 446},
    'Teresina': {'São Luís': 446, 'Fortaleza': 634, 'Palmas': 1164},
    'Fortaleza': {'Teresina': 634, 'Natal': 537, 'Recife': 800},
    'Natal': {'Fortaleza': 537, 'João Pessoa': 185, 'Recife': 286},
    'João Pessoa': {'Natal': 185, 'Recife': 120},
    'Recife': {'João Pessoa': 120, 'Maceió': 285, 'Fortaleza': 800, 'Natal': 286},
    'Maceió': {'Recife': 285, 'Aracaju': 294, 'Salvador': 632},
    'Aracaju': {'Maceió': 294, 'Salvador': 356},
    'Salvador': {'Aracaju': 356, 'Brasília': 1533, 'Belo Horizonte': 1372, 'Maceió': 632},
    'Palmas': {'Belém': 1269, 'Teresina': 1164, 'Brasília': 873, 'Goiânia': 874},
    'Brasília': {'Palmas': 873, 'Salvador': 1533, 'Belo Horizonte': 716, 'Goiânia': 209, 'Campo Grande': 1134, 'São Paulo': 872},
    'Goiânia': {'Brasília': 209, 'Cuiabá': 934, 'Campo Grande': 935, 'Palmas': 874},
    'Cuiabá': {'Goiânia': 934, 'Porto Velho': 1456, 'Campo Grande': 694},
    'Campo Grande': {'Cuiabá': 694, 'Goiânia': 900, 'Brasília': 1134, 'São Paulo': 1014, 'Curitiba': 991},
    'Belo Horizonte': {'Brasília': 716, 'Salvador': 1372, 'Vitória': 524, 'Rio de Janeiro': 434, 'São Paulo': 586},
    'Vitória': {'Belo Horizonte': 524, 'Rio de Janeiro': 521},
    'Rio de Janeiro': {'Belo Horizonte': 434, 'São Paulo': 429, 'Vitória': 521},
    'São Paulo': {'Rio de Janeiro': 429, 'Belo Horizonte': 586, 'Campo Grande': 1014, 'Curitiba': 408, 'Brasília': 872},
    'Curitiba': {'São Paulo': 408, 'Campo Grande': 991, 'Florianópolis': 300, 'Porto Alegre': 711},
    'Florianópolis': {'Curitiba': 300, 'Porto Alegre': 476},
    'Porto Alegre': {'Florianópolis': 476, 'Curitiba': 711},
    'Macapá': {'Belém': 308}
}

# Coordenadas geográficas para cálculo de distância
coordenadas_geograficas = {
    'Rio Branco': (-9.97499, -67.8243),
    'Porto Velho': (-8.76116, -63.9004),
    'Manaus': (-3.11903, -60.0217),
    'Boa Vista': (2.82384, -60.6753),
    'Belém': (-1.4554, -48.4898),
    'São Luís': (-2.52827, -44.2979),
    'Teresina': (-5.09201, -42.8038),
    'Fortaleza': (-3.71839, -38.5188),
    'Natal': (-5.79448, -35.211),
    'João Pessoa': (-7.1195, -34.845),
    'Recife': (-8.05224, -34.9286),
    'Maceió': (-9.66599, -35.7354),
    'Aracaju': (-10.9091, -37.0677),
    'Salvador': (-12.9722, -38.5014),
    'Palmas': (-10.2491, -48.3243),
    'Brasília': (-15.7801, -47.9292),
    'Goiânia': (-16.6864, -49.2643),
    'Cuiabá': (-15.6014, -56.0979),
    'Campo Grande': (-20.4428, -54.6458),
    'Belo Horizonte': (-19.9167, -43.9345),
    'Vitória': (-20.3191, -40.3378),
    'Rio de Janeiro': (-22.911, -43.2094),
    'São Paulo': (-23.5505, -46.6333),
    'Curitiba': (-25.4296, -49.2719),
    'Florianópolis': (-27.5945, -48.5477),
    'Porto Alegre': (-30.0331, -51.23),
    'Macapá': (0.03564, -51.0705)
}

def normalizar_texto(texto):
    """Remove acentos e caracteres especiais para comparação"""
    return normalize('NFKD', texto.lower()).encode('ASCII', 'ignore').decode('ASCII')

def validar_cidade(nome_cidade):
    """Verifica se a cidade existe no grafo"""
    nome_padronizado = normalizar_texto(nome_cidade)
    for cidade in conexoes_capitais.keys():
        if normalizar_texto(cidade) == nome_padronizado:
            return cidade
    return None

def calcular_distancia_haversine(lat1, lon1, lat2, lon2):
    """Calcula distância entre coordenadas usando fórmula de Haversine"""
    raio_terra = 6371  # km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return raio_terra * c

def distancia_entre_cidades(cidade1, cidade2):
    """Retorna distância em linha reta entre duas cidades"""
    lat1, lon1 = coordenadas_geograficas[cidade1]
    lat2, lon2 = coordenadas_geograficas[cidade2]
    return calcular_distancia_haversine(lat1, lon1, lat2, lon2)

def busca_largura(origem, destino):
    """Implementação BFS com contagem de operações"""
    fila = deque([(origem, [origem], 0)])
    visitados = {origem}
    operacoes = 0
    
    while fila:
        cidade_atual, caminho, distancia = fila.popleft()
        operacoes += 1
        
        if cidade_atual == destino:
            return caminho, distancia, operacoes
        
        for vizinho, dist in conexoes_capitais[cidade_atual].items():
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho], distancia + dist))
    
    return None, 0, operacoes

def busca_profundidade(origem, destino, limite=20):
    """Implementação DFS iterativa com limite"""
    pilha = [(origem, [origem], 0)]
    visitados = {origem}
    operacoes = 0
    
    while pilha:
        cidade_atual, caminho, distancia = pilha.pop()
        operacoes += 1
        
        if cidade_atual == destino:
            return caminho, distancia, operacoes
        
        if len(caminho) >= limite:
            continue
            
        for vizinho, dist in reversed(list(conexoes_capitais[cidade_atual].items())):
            if vizinho not in visitados:
                visitados.add(vizinho)
                pilha.append((vizinho, caminho + [vizinho], distancia + dist))
    
    return None, 0, operacoes

def busca_a_estrela(origem, destino):
    """Implementação A* com heurística de distância"""
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (0 + distancia_entre_cidades(origem, destino), 0, origem, [origem]))
    visitados = {}
    operacoes = 0
    
    while fila_prioridade:
        _, distancia_g, cidade_atual, caminho = heapq.heappop(fila_prioridade)
        operacoes += 1
        
        if cidade_atual == destino:
            return caminho, distancia_g, operacoes
        
        if cidade_atual in visitados and visitados[cidade_atual] <= distancia_g:
            continue
            
        visitados[cidade_atual] = distancia_g
        
        for vizinho, dist in conexoes_capitais[cidade_atual].items():
            nova_distancia = distancia_g + dist
            if vizinho not in visitados or nova_distancia < visitados.get(vizinho, float('inf')):
                heapq.heappush(fila_prioridade, 
                             (nova_distancia + distancia_entre_cidades(vizinho, destino),
                              nova_distancia,
                              vizinho,
                              caminho + [vizinho]))
    
    return None, 0, operacoes

def executar_algoritmo(algoritmo, origem, destino):
    """Seleciona e executa o algoritmo especificado"""
    if algoritmo == 'BFS':
        caminho, distancia, operacoes = busca_largura(origem, destino)
        nome = "Busca em Largura (BFS)"
    elif algoritmo == 'DFS':
        caminho, distancia, operacoes = busca_profundidade(origem, destino)
        nome = "Busca em Profundidade (DFS)"
    elif algoritmo == 'A*':
        caminho, distancia, operacoes = busca_a_estrela(origem, destino)
        nome = "Busca A* (Heurística)"
    
    return {
        'algoritmo': nome,
        'caminho': caminho,
        'distancia': distancia,
        'operacoes': operacoes
    }

def formatar_resultado(resultado):
    """Formata os resultados para exibição"""
    if not resultado['caminho']:
        return f"{resultado['algoritmo']}: Rota não encontrada\n"
    
    output = f"\n=== {resultado['algoritmo']} ===\n"
    output += f"Rota: {' → '.join(resultado['caminho'])}\n"
    output += f"Distância total: {resultado['distancia']} km\n"
    output += f"Operações realizadas: {resultado['operacoes']}\n"
    return output

def comparar_algoritmos(origem, destino):
    """Executa e compara os três algoritmos"""
    print(f"\nComparação: {origem} → {destino}")
    
    algoritmos = ['BFS', 'DFS', 'A*']
    resultados = []
    
    for algo in algoritmos:
        resultados.append(executar_algoritmo(algo, origem, destino))
    
    # Exibir resultados individuais
    for res in resultados:
        print(formatar_resultado(res))
    
    # Tabela comparativa
    print("\nRESUMO COMPARATIVO")
    print(f"{'Algoritmo':<25} | {'Distância (km)':>15} | {'Operações':>10}")
    print("-" * 60)
    for res in resultados:
        if res['caminho']:
            print(f"{res['algoritmo']:<25} | {res['distancia']:>15.2f} | {res['operacoes']:>10}")
        else:
            print(f"{res['algoritmo']:<25} | {'-':>15} | {'-':>10}")

def menu_principal():
    """Interface do usuário"""
    print("SISTEMA DE ROTEAMENTO ENTRE CAPITAIS BRASILEIRAS")
    print("Capitais disponíveis:")
    for capital in sorted(conexoes_capitais.keys()):
        print(f"- {capital}")
    
    # Obter origem
    while True:
        origem = validar_cidade(input("\nDigite a cidade de origem: ").strip())
        if origem:
            break
        print("Cidade inválida. Tente novamente.")
    
    # Obter destino
    while True:
        destino = validar_cidade(input("Digite a cidade de destino: ").strip())
        if destino:
            break
        print("Cidade inválida. Tente novamente.")
    
    # Seleção de modo
    print("\nOpções:")
    print("1. Usar método de busca específico")
    print("2. Comparar todos os métodos de buscas")
    opcao = input("Escolha (1-2): ").strip()
    
    if opcao == '1':
        print("\nMétodos de buscas disponíveis:")
        print("1. Busca em Largura (BFS)")
        print("2. Busca em Profundidade (DFS)")
        print("3. Busca A* (Distância em linha reta)")
        escolha = input("Selecione (1-3): ").strip()
        
        if escolha == '1':
            resultado = executar_algoritmo('BFS', origem, destino)
        elif escolha == '2':
            resultado = executar_algoritmo('DFS', origem, destino)
        elif escolha == '3':
            resultado = executar_algoritmo('A*', origem, destino)
        else:
            print("Opção inválida!")
            return
        
        print(formatar_resultado(resultado))
        
    elif opcao == '2':
        comparar_algoritmos(origem, destino)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()