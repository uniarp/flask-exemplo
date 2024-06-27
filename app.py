from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/tutor') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "cpf": "000.000.000-00",
        "nome": "Serjao Berranteiro",
        "data_nascimento": "1712275315",
        "email": "sergo12345cacadorbaum@yahoo.com",
        "telefone": "49 99999-9999",
        "endereco": "Rua Barretos n222",
        "cons_cadun": "https://imgur.com/gallery/KezmxiX"
    }
    return [resultado]