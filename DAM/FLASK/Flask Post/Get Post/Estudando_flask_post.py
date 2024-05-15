from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

pessoas = [
    {"nome": "Paulo", "sexo": "M", "cabelo": "loiro"},
    {"nome": "Maria", "sexo": "F", "cabelo": "preto"},
    {"nome": "Fernanda", "sexo": "F", "cabelo": "ruivo"},
    {"nome": "José", "sexo": "M", "cabelo": "careca"}
]

#consultar como esta sendo enviado as informações para o servidor
def pessoa_ok(dic):
    return type(dic) == dict \
        and len(dic) == 3 \
        and "nome" in dic \
        and "sexo" in dic \
        and "cabelo" in dic \
        and type(dic["nome"]) == str \
        and dic["sexo"] in ["M", "F"] \
        and type(dic["cabelo"]) == str

@app.route("/pessoas", methods=["GET"])
def consulta_pessoas():
    return(pessoas)

@app.route("/pessoa", methods = ["POST"])
def cadastrar():
    pessoa = request.json
    if not pessoa_ok(pessoa):#testando se esta ok o dicionario
        raise BadRequest
    pessoas.append(pessoa)
    return jsonify(pessoas)

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000)