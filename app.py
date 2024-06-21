from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/AnimalParaAdocao') # URL, path, rota, caminho, link, URI
def animal():
    resultado = {
        "nomeDoAnimal": "pitoco",
        "especieDoAnimal": "felino",
        "corPredominanteDoAnimal": "preto",
        "dadosDeNascimentoDoAnimal": "15/05/1997",
        "racaDoAnimal": "Lulu da pomerânia"
    }
    return resultado
