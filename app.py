from flask import Flask, request

app = Flask(__name__)


# http://127.0.0.1:5000/

@app.route('/historico_clinico') # url, path, rota, caminho, link, uri
def historico_clinico():
    resultado =  {
        "Nome_tutor": "Daniel",
        "nome_animal": "Bolo",
        "data_agendada": "24/04/2019",

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

@app.route('/tutor') # url, path, rota, caminho, link, uri
def tutor():
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