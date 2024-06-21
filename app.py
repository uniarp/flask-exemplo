from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "Nome": "Daniel"
    }
    return [resultado]

@app.route('/consulta')
def consulta():
    resultado = {
    "motivo_atendimento": "atropelamento",
    "diagnostico": "costela quebra",
    "tratamento_recomendado": "imobilização por 7 dias",
    "observacao": "animal com diabete",
    "Id_animal": "456",
    "data_hora": "1711813393"
    }
    return resultado


