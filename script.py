# Inicialização de variáveis
acolitos = []  # Lista para armazenar informações dos acólitos

# Dicionário para associar funções a pontuações
pontuacoes_funcoes = {
    "turibulo": 0,
    "missal": 2,
    "credencia": 3,
    "ambao": 4,
    "sino": 5,
    "acompanhante": 6,
}

# Verificação do uso do turíbulo
usar_turibulo = input("Olá, sou AcolitApp, seu gerenciador de funções para a Missa.\nHoje nós usaremos o turíbulo? (S/N): ").strip().lower() == "s"

# Quantidade de acólitos
quantidade_acolitos = int(input("Quantos acólitos irão servir hoje?! "))

# Coleta de informações de cada acólito
for i in range(quantidade_acolitos):
    nome_acolito = input(f"Qual o nome do acólito {i + 1}: ")
    funcao_anterior = input(f"Qual a função anterior de {nome_acolito}? ").strip().lower()
    
    # Se a função anterior for "banco" ou em branco, atribua a maior pontuação
    if funcao_anterior == "banco" or funcao_anterior == "":
        pontuacao_funcao_anterior = 8
    else:
        # Caso contrário, obtenha a pontuação da função anterior do dicionário
        pontuacao_funcao_anterior = pontuacoes_funcoes.get(funcao_anterior, 0)
    
    ordem_chegada = int(input(f"Qual a ordem de chegada de {nome_acolito}? "))

    # Calcula a pontuação com base na função anterior e na ordem de chegada
    pontuacao_ordem_chegada = quantidade_acolitos - ordem_chegada + 1
    pontuacao_total = pontuacao_funcao_anterior + pontuacao_ordem_chegada

    # Cria um dicionário para representar o acólito e armazena suas informações e pontuação
    acolito = {
        "nome": nome_acolito,
        "funcao_anterior": funcao_anterior,
        "ordem_chegada": ordem_chegada,
        "pontuacao": pontuacao_total,
    }

    # Adiciona o acólito à lista de acólitos
    acolitos.append(acolito)

# Exibição das informações coletadas
print("\nInformações dos acólitos e suas pontuações:")
for i, acolito in enumerate(acolitos, start=1):
    print(f"Acólito {i}:")
    print(f"Nome: {acolito['nome']}")
    print(f"Função anterior: {acolito['funcao_anterior']}")
    print(f"Ordem de chegada: {acolito['ordem_chegada']}")
    print(f"Pontuação: {acolito['pontuacao']}")
    print()

# Cria uma lista de funções disponíveis
funcoes_disponiveis = []

if usar_turibulo:
    funcoes_disponiveis.append("turibulo")
funcoes_disponiveis.extend(["missal", "credencia", "ambao", "sino", "acompanhante"])

# Ordena os acólitos com base nas pontuações, do maior para o menor
acolitos_ordenados = sorted(acolitos, key=lambda x: x["pontuacao"], reverse=True)

# Atribui funções aos acólitos
funcoes_atribuidas = {}
funcoes_utilizadas = set()

for acolito in acolitos_ordenados:
    for funcao in funcoes_disponiveis:
        if funcao not in funcoes_utilizadas:
            funcoes_atribuidas[acolito["nome"]] = funcao
            funcoes_utilizadas.add(funcao)
            break
    else:
        funcoes_atribuidas[acolito["nome"]] = "banco"

# Exibe as funções atribuídas aos acólitos
print("\nAlocação de funções para a próxima missa:")
for nome_acolito, funcao in funcoes_atribuidas.items():
    print(f"{nome_acolito}: {funcao}")


