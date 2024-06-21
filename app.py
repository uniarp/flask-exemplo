from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/cadastrar_Doencas') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "id_doenca": "123",
        "nome_doença": "Ehrlichiose",
        "sintomas": "apatia, febre, vômito",
        "tratamentos_associado": "antibióticos",
    }
    return [resultado]