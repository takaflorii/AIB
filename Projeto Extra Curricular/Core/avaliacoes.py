def adicionar_avaliacao(dados, disciplina, tipo, data):
    avaliacao = {
        "disciplina": disciplina,
        "tipo": tipo,
        "data": data,
        "nota": None
    }
    dados["avaliacoes"].append(avaliacao)

def listar_avaliacoes(dados):
    return dados["avaliacoes"]

def avaliacoes_por_disciplina(dados, nome_disciplina):
    return [
        a for a in dados["avaliacoes"]
        if a["disciplina"].lower() == nome_disciplina.lower()
    ]
