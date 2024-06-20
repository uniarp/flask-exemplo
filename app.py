from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "Nome": "Gustavo"
    }
    return [resultado]