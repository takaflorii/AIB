def registar_estudo(dados, disciplina, minutos):
    estudo = {
        "disciplina": disciplina,
        "minutos": minutos
    }
    dados["estudos"].append(estudo)

def total_estudo_disciplina(dados, nome_disciplina):
    total = 0
    for e in dados["estudos"]:
        if e["disciplina"].lower() == nome_disciplina.lower():
            total += e["minutos"]
    return total
