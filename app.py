from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "Nome": "Daniel"
    }
    return [resultado]

@app.route('/cadastrartutor')
def salvar():
    resultado = {
        "nome_animal" : "Carreta",
        "especie" : "cachoro",
        "raca" : "São Bernado",
        "peso" : "67 Kg",
        "idade" : "2 anos",
        "rfid" : "1711813393"
    }
    return [resultado]