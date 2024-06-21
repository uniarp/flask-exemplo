from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "Atendimento"
        "motivo_atendimento: atropelamento",
        "observacao: alergia alimentar",
        "Id_animal: 01234",
        "data_hora: 10:30",
    }
