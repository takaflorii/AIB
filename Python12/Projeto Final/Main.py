from Ficheiros import guardar_dados, carregar_dados

dados = {
    'Disciplinas': [],
    'Avaliações': [],
    'Estudos': []
}

ficheiros= carregar_dados()


def menu():
    print("=== Menu Principal ===")
    print("1. Adicionar Disciplina")
    print("2. Adicionar avaliação")
    print("3. Registar estudo")
    print("4. Consultar dados")
    print("0. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print("Opção para adicionar disciplina selecionada.")
        # Código para adicionar disciplina aqui
    elif escolha == '2':
        print("Opção para adicionar avaliação selecionada.")
        # Código para adicionar avaliação aqui
    elif escolha == '3':
        print("Opção para registar estudo selecionada.")
        # Código para registar estudo aqui
    elif escolha == '4':
        print("Opção para consultar dados selecionada.")
        # Código para consultar dados aqui
    elif escolha == '0':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
