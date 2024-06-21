from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/animal') # url, path, rota, caminho, link, uri
def animal():
    resultado = {
        'nome_animal': "Carreta",
        'especie': "cachoro",
        'raca': "São Bernado",
        'peso': "67 Kg",
        'idade': "2 anos",
        'rfid': "1711813393"
        }
    return [resultado]