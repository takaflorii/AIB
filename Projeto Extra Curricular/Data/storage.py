import json
import os

# Get the correct path to dados.json
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FICHEIRO = os.path.join(SCRIPT_DIR, "..", "dados.json")

def carregar_dados():
    try:
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "disciplinas": [],
            "avaliacoes": [],
            "estudos": []
        }

def guardar_dados(dados):
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
