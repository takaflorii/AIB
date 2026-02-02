import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, redirect, url_for

# Import from modules
import Core.disciplinas as disc_module
import Core.avaliacoes as aval_module
import Core.estudos as est_module
import Data.storage as storage_module

adicionar_disciplina = disc_module.adicionar_disciplina
listar_disciplinas = disc_module.listar_disciplinas
adicionar_avaliacao = aval_module.adicionar_avaliacao
listar_avaliacoes = aval_module.listar_avaliacoes
avaliacoes_por_disciplina = aval_module.avaliacoes_por_disciplina
registar_estudo = est_module.registar_estudo
total_estudo_disciplina = est_module.total_estudo_disciplina
guardar_dados = storage_module.guardar_dados
carregar_dados = storage_module.carregar_dados

# Create Flask app with explicit template folder
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# Estado da aplicação (carregado ao iniciar o servidor)
dados = carregar_dados()


@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <title>A12 Gestor de Estudos</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: Arial, sans-serif; background-color: #f5f5f5; color: #333; }
            header { background-color: #2c3e50; color: white; padding: 20px; text-align: center; }
            header h1 { margin-bottom: 10px; }
            nav { display: flex; justify-content: center; gap: 20px; }
            nav a { color: white; text-decoration: none; padding: 10px 15px; border-radius: 4px; }
            nav a:hover { background-color: #34495e; }
            main { max-width: 800px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; }
            h2 { margin-bottom: 20px; color: #2c3e50; }
            p { line-height: 1.6; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <header>
            <h1>A12 Gestor de Estudos</h1>
            <nav>
                <a href="/">Início</a>
                <a href="/disciplinas">Disciplinas</a>
                <a href="/avaliacoes">Avaliações</a>
                <a href="/estudos">Estudos</a>
            </nav>
        </header>
        <main>
            <h2>Bem-vindo ao A12 Gestor de Estudos</h2>
            <p>Esta aplicação ajuda-te a organizar disciplinas, avaliações e tempo de estudo de forma simples e eficiente.</p>
            <p>Usa o menu acima para começares.</p>
        </main>
    </body>
    </html>
    """
    return html


@app.route("/disciplinas", methods=["GET", "POST"])
def disciplinas():
    if request.method == "POST":
        nome = request.form["nome"]
        adicionar_disciplina(dados, nome)
        guardar_dados(dados)
        return redirect(url_for("disciplinas"))

    lista = listar_disciplinas(dados)
    
    disciplinas_html = "".join([f"<li>{d['nome']}</li>" for d in lista]) if lista else "<li>Nenhuma disciplina registada.</li>"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <title>Disciplinas</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: Arial, sans-serif; background-color: #f1f6f2; color: #213323; }}
            header {{ background-color: #2f5d3a; color: white; padding: 20px; text-align: center; }}
            header h1 {{ margin-bottom: 10px; }}
            nav {{ display: flex; justify-content: center; gap: 20px; }}
            nav a {{ color: white; text-decoration: none; padding: 10px 15px; border-radius: 4px; }}
            nav a:hover {{ background-color: #27462f; }}
            main {{ max-width: 800px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; }}
            h2 {{ margin-bottom: 20px; color: #234f2b; }}
            form {{ display: flex; gap: 10px; margin-bottom: 20px; }}
            input, button {{ padding: 10px; border: 1px solid #ddd; border-radius: 4px; }}
            button {{ background-color: #2e7a42; color: white; cursor: pointer; }}
            button:hover {{ background-color: #256233; }}
            ul {{ list-style: none; }}
            li {{ padding: 10px; border-bottom: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <header>
            <h1>A12 Gestor de Estudos</h1>
            <nav>
                <a href="/">Início</a>
                <a href="/disciplinas">Disciplinas</a>
                <a href="/avaliacoes">Avaliações</a>
                <a href="/estudos">Estudos</a>
            </nav>
        </header>
        <main>
            <h2>Disciplinas</h2>
            <form method="POST">
                <input type="text" name="nome" placeholder="Nome da Disciplina" required>
                <button type="submit">Adicionar Disciplina</button>
            </form>
            <ul>
                {disciplinas_html}
            </ul>
        </main>
    </body>
    </html>
    """
    return html


@app.route("/avaliacoes", methods=["GET", "POST"])
def avaliacoes():
    if request.method == "POST":
        disciplina = request.form["disciplina"]
        tipo = request.form["tipo"]
        data = request.form["data"]
        adicionar_avaliacao(dados, disciplina, tipo, data)
        guardar_dados(dados)
        return redirect(url_for("avaliacoes"))
    
    lista = listar_avaliacoes(dados)
    avaliacoes_html = "".join([f"<li>{a['disciplina']} — {a['tipo']} ({a['data']})</li>" for a in lista]) if lista else "<li>Nenhuma avaliação registada.</li>"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <title>Avaliações</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: Arial, sans-serif; background-color: #f1f6f2; color: #213323; }}
            header {{ background-color: #2f5d3a; color: white; padding: 20px; text-align: center; }}
            header h1 {{ margin-bottom: 10px; }}
            nav {{ display: flex; justify-content: center; gap: 20px; }}
            nav a {{ color: white; text-decoration: none; padding: 10px 15px; border-radius: 4px; }}
            nav a:hover {{ background-color: #27462f; }}
            main {{ max-width: 800px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; }}
            h2 {{ margin-bottom: 20px; color: #234f2b; }}
            form {{ display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px; }}
            input, select, button {{ padding: 10px; border: 1px solid #ddd; border-radius: 4px; }}
            button {{ background-color: #2e7a42; color: white; cursor: pointer; }}
            button:hover {{ background-color: #256233; }}
            ul {{ list-style: none; }}
            li {{ padding: 10px; border-bottom: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <header>
            <h1>A12 Gestor de Estudos</h1>
            <nav>
                <a href="/">Início</a>
                <a href="/disciplinas">Disciplinas</a>
                <a href="/avaliacoes">Avaliações</a>
                <a href="/estudos">Estudos</a>
            </nav>
        </header>
        <main>
            <h2>Avaliações</h2>
            <form method="POST">
                <input type="text" name="disciplina" placeholder="Nome da Disciplina" required>
                <select name="tipo" required>
                    <option value="">Selecionar tipo</option>
                    <option value="Teste">Teste</option>
                    <option value="Trabalho">Trabalho</option>
                    <option value="Exame">Exame</option>
                </select>
                <input type="date" name="data" required>
                <button type="submit">Adicionar Avaliação</button>
            </form>
            <ul>
                {avaliacoes_html}
            </ul>
        </main>
    </body>
    </html>
    """
    return html


@app.route("/estudos", methods=["GET", "POST"])
def estudos():
    if request.method == "POST":
        disciplina = request.form["disciplina"]
        minutos = int(request.form["minutos"])
        registar_estudo(dados, disciplina, minutos)
        guardar_dados(dados)
        return redirect(url_for("estudos"))
    
    lista = listar_avaliacoes(dados)
    estudos_html = "".join([f"<li>{e['disciplina']} — {e['minutos']} minutos</li>" for e in dados["estudos"]]) if dados["estudos"] else "<li>Nenhum registo de estudo.</li>"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <title>Estudos</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: Arial, sans-serif; background-color: #f1f6f2; color: #213323; }}
            header {{ background-color: #2f5d3a; color: white; padding: 20px; text-align: center; }}
            header h1 {{ margin-bottom: 10px; }}
            nav {{ display: flex; justify-content: center; gap: 20px; }}
            nav a {{ color: white; text-decoration: none; padding: 10px 15px; border-radius: 4px; }}
            nav a:hover {{ background-color: #27462f; }}
            main {{ max-width: 800px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; }}
            h2 {{ margin-bottom: 20px; color: #234f2b; }}
            form {{ display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px; }}
            input, button {{ padding: 10px; border: 1px solid #ddd; border-radius: 4px; }}
            button {{ background-color: #2e7a42; color: white; cursor: pointer; }}
            button:hover {{ background-color: #256233; }}
            ul {{ list-style: none; }}
            li {{ padding: 10px; border-bottom: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <header>
            <h1>A12 Gestor de Estudos</h1>
            <nav>
                <a href="/">Início</a>
                <a href="/disciplinas">Disciplinas</a>
                <a href="/avaliacoes">Avaliações</a>
                <a href="/estudos">Estudos</a>
            </nav>
        </header>
        <main>
            <h2>Tempo de Estudo</h2>
            <form method="POST">
                <input type="text" name="disciplina" placeholder="Nome da Disciplina" required>
                <input type="number" name="minutos" placeholder="Minutos de estudo" min="1" required>
                <button type="submit">Registar Estudo</button>
            </form>
            <ul>
                {estudos_html}
            </ul>
        </main>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    app.run(debug=True)

