from flask import Flask, jsonify

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
@app.route('/AnimalParaAdocao') # URL, path, rota, caminho, link, URI
def AnimalParaAdocao():
    resultado = {
        "nomeDoAnimal": "pitoco",
        "especieDoAnimal": "felino",
        "corPredominanteDoAnimal": "preto",
        "dadosDeNascimentoDoAnimal": "15/05/1997",
        "racaDoAnimal": "Lulu da pomerânia"
    }
    return resultado
# http://127.0.0.1:5000/

@app.route('/historico_clinico') # url, path, rota, caminho, link, uri
def historico_clinico():
    resultado =  {
        "Nome_tutor": "Daniel",
        "nome_animal": "Bolo",
        "data_agendada": "24/04/2019",
    }
    return [resultado]
# http://127.0.0.1:5000/soma?a=10&b=15
@app.route('/cadastrar_Doencas') # url, path, rota, caminho, link, uri
def inicio():
    resultado =  {
        "id_doenca": "123",
        "nome_doença": "Ehrlichiose",
        "sintomas": "apatia, febre, vômito",
        "tratamentos_associado": "antibióticos"
    }
    return [resultado]
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

@app.route('/consulta')
def consulta():
    resultado = {
    "motivo_atendimento": "atropelamento",
    "diagnostico": "costela quebra",
    "tratamento_recomendado": "imobilização por 7 dias",
    "observacao": "animal com diabete",
    "Id_animal": "456",
    "data_hora": "1711813393"
    }
    return [resultado]

@app.route('/cadastrartutor')
def salvar():
    resultado = {
        "nome_animal" : "Carreta",
        "especie" : "cachoro",
        "raca" : "São Bernado",
        "peso" : "67 Kg",
        "idade" : "2 anos",
        "rfid" : "1711813393"
    }
    return [resultado]



@app.route('/cadastraranimal') # url, path, rota, caminho, link, uri
def cadastraranimal():
    resultado =  {
        
        
        "nome_aniaml":"Tusk",
        "especie": "Cachorro",
        "raça": "Pastor-Alemão 2",
        "sexo": "Macho",
        "peso": "30Kg", 
        "idade_estimada": "7 anos",
        "historico_clinico": "Animal com vacinação em dia"

    }
    return [resultado
    
    ]