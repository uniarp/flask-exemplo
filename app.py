from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/Denuncia') # url, path, rota, caminho, link, uri
def denuncia():
    resultado =  {
        "Endereço" : "Caçador SC",
        "Bairro" : "Gioppo",
        "Observação" : "Maus Tratos"
    }
    return [resultado]