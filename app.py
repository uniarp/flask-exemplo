from flask import Flask, request

app = Flask(__name__)

# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/divulgacao') # url, path, rota, caminho, link, uri
def campanhaAnimal():
    resultado =  [{
        "Dados do Evento": "25/07/2024",
        "Horário do Evento" : "14:00",
        "Local do Evento" : "Parque Das Araucarias",
        "Imagem" : "Image.png"
    }, {
        "Dados do Evento": "20/09/2024",
        "Horário do Evento" : "15:00",
        "Local do Evento" : "Parque Central",
        "Imagem1" : "Image1.png",
    }, {
        "Dados do Evento": "28/10/2024",
        "Horário do Evento" : "17:00",
        "Local do Evento" : "Parque Das Araucarias",
        "Imagem2" : "Image2.png",
    }]
    return [resultado]
