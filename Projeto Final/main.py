from Data.Storage import guardar_dados, carregar_dados
from Core.Disciplinas import adicionar_disciplina
from Core.Avaliacoes import adicionar_avaliacao
from Core.Estudos import registar_estudo

def menu():
    print("\n=== Menu Principal ===")
    print("1. Adicionar Disciplina")
    print("2. Adicionar Avaliação")
    print("3. Registar Estudo")
    print("4. Consultar Dados")
    print("0. Sair")

dados = carregar_dados()

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_disciplina(dados)
    elif escolha == "2":
        adicionar_avaliacao(dados)
    elif escolha == "3":
        registar_estudo(dados)
    elif escolha == "4":
        print(dados)
    elif escolha == "0":
        guardar_dados(dados)
        print("Até logo!")
        break
    else:
        print("Opção inválida.")
