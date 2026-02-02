def adicionar_disciplina(nome):
    nome = input("Digite o nome da disciplina: ")

    disciplina = {
        'nome': nome
    }

    dados['Disciplinas'].append(disciplina)
    print(f"Disciplina '{nome}' adicionada com sucesso!")
