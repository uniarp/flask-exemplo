from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/

@app.route('/historico_clinico') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "Nome_tutor": "Daniel",
        "nome_animal": "Bolo",
        "data_agendada": "24/04/2019",
    }
    return [resultado]