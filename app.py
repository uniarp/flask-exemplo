from flask import Flask, jsonify

app = Flask(__name__)
# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/cadastrar_Doencas') # url, path, rota, caminho, link, uri
def inicio():
    resultado = [
    {
        "id_doenca": "123",
        "nome_doença": "Ehrlichiose",
        "sintomas": "apatia, febre, vômito",
        "tratamentos_associado": "antibióticos"
    },
    {
        "id_doenca": "456",
        "nome_doenca": "Rinotraqueíte Felina",
        "sintomas": "espirros, secreção ocular, febre",
        "tratamentos_associados": "antibióticos, suporte sintomático"
    },
    {
        "id_doenca": "789",
        "nome_doenca": "Leishmaniose Canina",
        "sintomas": "lesões de pele, perda de peso, febre",
        "tratamentos_associados": "tratamento específico, controle de vetores"
    },
    {
        "id_doenca": "101",
        "nome_doenca": "Peritonite Infecciosa Felina",
        "sintomas": "dor abdominal, letargia, febre",
        "tratamentos_associados": "tratamento sintomático, cuidados de suporte"
    }
]
    return jsonify(resultado)
if __name__ == '__main__':
        app.run(debug=True)