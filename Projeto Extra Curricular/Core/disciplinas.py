def adicionar_disciplina(dados, nome):
    disciplina = {
        "nome": nome
    }
    dados["disciplinas"].append(disciplina)

def listar_disciplinas(dados):
    return dados["disciplinas"]

def disciplina_existe(dados, nome):
    for d in dados["disciplinas"]:
        if d["nome"].lower() == nome.lower():
            return True
    return False
