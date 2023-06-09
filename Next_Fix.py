# Implementação do next-fit - André Moura
def next_fit(memoria, tamanho_memoria, solicitacoes, tamanho_solicitacoes, nomes_solicitacoes):
    alocado = []  # Lista para armazenar as solicitações alocadas
    tamanho_alocado = 0  # Contador para o número de solicitações alocadas
    memoria_restante = memoria.copy()  # Cria uma cópia da lista de memória
    fragmentacao_externa = 0  # Armazena a fragmentação externa acumulada
    fragmentacao_interna = 0  # Armazena a fragmentação interna acumulada
    memoria_livre = 0  # Armazena a quantidade de memória livre

    ultimo_indice_alocado = 0  # Índice da última lacuna alocada

    alocacoes_individuais = []  # Lista para armazenar as alocações individuais

    # Itera sobre as solicitações de memória
    for i in range(tamanho_solicitacoes):
        indice_alocado = -1

        # Começar a busca pela alocação a partir da última lacuna alocada
        for j in range(ultimo_indice_alocado, tamanho_memoria):
            if memoria_restante[j] >= solicitacoes[i]:
                indice_alocado = j
                break

        if indice_alocado == -1:
            # Se não houver uma lacuna disponível a partir da última alocada,
            # volte ao início da memória e procure por uma lacuna.
            for j in range(tamanho_memoria):
                if memoria_restante[j] >= solicitacoes[i]:
                    indice_alocado = j
                    break
            if indice_alocado == -1:
                continue

        # Alocando a solicitação encontrada na lacuna de memória
        alocado.append((nomes_solicitacoes[i], solicitacoes[i], indice_alocado))
        tamanho_alocado += 1
        memoria_restante[indice_alocado] -= solicitacoes[i]
        fragmentacao_interna += memoria_restante[indice_alocado]

        # Atualiza o índice da última lacuna alocada
        ultimo_indice_alocado = (indice_alocado + 1) % tamanho_memoria

        # Calcula a fragmentação externa acumulada
        for k in range(ultimo_indice_alocado):
            if memoria_restante[k] > 0:
                fragmentacao_externa += memoria_restante[k]

        # Armazena a alocação individual
        alocacoes_individuais.append(str(memoria_restante))

    memoria_livre = sum(memoria_restante)  # Calcula a memória livre
    # Retorna as informações da alocação de memória
    return alocado, memoria_restante, fragmentacao_externa, fragmentacao_interna, memoria_livre, alocacoes_individuais


# Entrada de dados
memoria_total = int(input("Digite o tamanho total da memória em KB: "))
tamanho_memoria = int(input("Digite o número de lacunas de memória em KB: "))
memoria = []
print("Digite os tamanhos das lacunas de memória em KB:")
for i in range(tamanho_memoria):
    tamanho = int(input("Lacuna KB {}: ".format(i + 1)))
    memoria.append(tamanho)


tamanho_solicitacoes = int(input("Digite o número de solicitações em KB: "))
solicitacoes = []
nomes_solicitacoes = []
print("Digite os tamanhos e nomes das solicitações em KB:")
for i in range(tamanho_solicitacoes):
    tamanho = int(input("Tamanho da solicitação KB {}: ".format(i + 1)))
    nome = input("Nome da solicitação {}: ".format(i + 1))
    solicitacoes.append(tamanho)
    nomes_solicitacoes.append(nome)

# Chamada da função next_fit para alocar memória
alocado, memoria_restante, fragmentacao_externa, fragmentacao_interna, memoria_livre, alocacoes_individuais = next_fit(
    memoria, tamanho_memoria, solicitacoes, tamanho_solicitacoes, nomes_solicitacoes
)

# Impressão dos resultados
print("\n--- Resultados ---")
print("Solicitações alocadas:")
for nome, tamanho, indice_lacuna in alocado:
    print("Nome:", nome, "- Tamanho:", tamanho, "- Lacuna:", indice_lacuna)
print("Tamanho total da memória:", memoria_total, "KB")
print("Tamanho de memória anterior:", memoria)
for i in range(tamanho_solicitacoes):
    print("Resultado da Alocação", i+1, ":", alocacoes_individuais[i])
print("Fragmentação externa dos processos:", fragmentacao_externa)
print("Fragmentação interna:", fragmentacao_interna)
print("Memória livre:", memoria_livre)
