# Funções disponíveis em ordem de importância
funcoes = ["turibulo", "missal", "credencia", "ambao", "acompanhante", "sino"]

# Verificar se o turíbulo será utilizado
tem_turibulo = input("Haverá turíbulo na próxima missa? (S/N): ").strip().lower() == "s"

# Solicitar o número de acólitos que participarão
num_acolitos = int(input("Quantos acólitos participarão da próxima missa? "))

# Lista de acólitos e ordem de chegada
acolitos = []
ordem_chegada = []

# Coletar informações sobre cada acólito
for i in range(num_acolitos):
    nome = input(f"Nome do acólito {i + 1}: ")
    ordem = int(input(f"Ordem de chegada do(a) {nome}: "))
    funcao_anterior = input(f"Função anterior de {nome} (ou deixe em branco): ")

    # Adicionar o acólito à lista de ordem de chegada
    ordem_chegada.append(nome)

    acolito = {
        "nome": nome,
        "ordem_chegada": ordem,
        "funcao_anterior": funcao_anterior if funcao_anterior in funcoes else None,
    }

    acolitos.append(acolito)

# Função para calcular a pontuação de um acólito
def calcular_pontuacao(acolito):
    pontuacao = 0

    # Se a função anterior não foi especificada, atribua a pontuação máxima
    if acolito["funcao_anterior"] is None:
        pontuacao += len(funcoes)
    else:
        # Se a função anterior foi especificada, atribua a pontuação com base na função
        # Invertemos a pontuação da função anterior (quanto melhor a função anterior, menor a pontuação)
        pontuacao += (len(funcoes) - funcoes.index(acolito["funcao_anterior"]))

    # Atribua uma pontuação adicional com base na ordem de chegada (quanto mais tarde, menor a pontuação)
    pontuacao -= ordem_chegada.index(acolito["nome"])

    return pontuacao

# Classificar os acólitos com base na pontuação
acolitos_ordenados = sorted(acolitos, key=calcular_pontuacao, reverse=True)

# Atribuir funções aos acólitos
for i, acolito in enumerate(acolitos_ordenados):
    if i < len(funcoes):
        acolito["funcao_atual"] = funcoes[i]
    else:
        acolito["funcao_atual"] = "sem função disponível"

# Exibir a alocação de funções
print("\nAlocação de funções para a próxima missa:")
for acolito in acolitos_ordenados:
    print(f"{acolito['nome']}: {acolito['funcao_atual']}")
