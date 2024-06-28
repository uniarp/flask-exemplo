from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/divulgacao') # url, path, rota, caminho, link, uri
def campanhaAnimal1():
    resultado =  {
        "Dados do Evento": "20/09/2024",
        "Horário do Evento" : "15:00",
        "Local do Evento" : "Parque Central",
        "Imagem" : "Image.png"
    }
    return [resultado]

@app.route('/divulgacao2')
def campanhaAnimal2():
    resultado =  {
        "Dados do Evento": "25/07/2024",
        "Horário do Evento" : "14:00",
        "Local do Evento" : "Parque Das Araucarias",
        "Imagem" : "Image.png"
    }
    return [resultado]
