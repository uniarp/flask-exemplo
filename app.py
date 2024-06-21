from flask import Flask, request

app = Flask(__name__)


# http://127.0.0.1:5000/cadastrarTutor
@app.route('/cadastrarTutor')
def cadastrarTutor():
    resultado = {
        "id_tutor": "321",
        "nome": "Gustavo Miguel",
        "endereço": "Rua Avenidade Paulista, N70",
        "telefone": "49912345678",
        "email": "gustavomiguel0312@gmail.com"
        }
    return [resultado]