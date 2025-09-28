# Função para cadastrar notas
def cadastrar_notas():
    while True:
        entrada = input("Digite as notas do aluno separadas por espaço (ou 'sair' para voltar): ")
        if entrada.lower() == 'sair':
            return None  # Retorna None para indicar que o usuário quer voltar
        try:
            # Converte cada valor digitado em float e cria uma lista de notas
            notas = [float(n) for n in entrada.split()]
            return notas
        except ValueError:
            print("Entrada inválida! Digite números separados por espaço ou 'sair'.")

# Função para calcular a média
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função para determinar situação do aluno
def situacao_aluno(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Função para exibir relatório final
def exibir_relatorio(notas, media, situacao):
    print("\n===== RELATÓRIO FINAL =====")
    print("Notas inseridas:", notas)
    print(f"Média: {media:.2f}")
    print("Situação:", situacao)

# Programa principal
print("=== Sistema de Gestão de Notas ===")

while True:
    nome_aluno = input("\nDigite o nome do aluno (ou 'sair' para encerrar): ")
    if nome_aluno.lower() == 'sair':
        print("\nSistema finalizado.")
        break  # Encerra o programa

    notas = cadastrar_notas()  # Solicita as notas separadas por espaço
    if notas is None:  # Se o usuário digitou "sair" nas notas
        continue  # Volta para perguntar o nome do aluno

    if len(notas) == 0:
        print("Nenhuma nota registrada para este aluno.")
        continue  # Volta para o menu de alunos

    media = calcular_media(notas)
    situacao = situacao_aluno(media)
    print(f"\nRelatório do aluno: {nome_aluno}")
    exibir_relatorio(notas, media, situacao)
