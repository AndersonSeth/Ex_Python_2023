#rotas para,etrizadas

from flask import Flask
app = Flask(__name__)

cores_frutas = {
    "morango": "vermelho",
    "uva": "roxo",
    "banana": "amarelo",
    "abacaxi": "vamarelo",
    "limão": "verde",

}
@app.route("/")
@app.route("/frutas/<nome_fruta>/cor")
def frutas(nome_fruta):
    if nome_fruta in cores_frutas:
        return cores_frutas[nome_fruta]
    return "Não Sei"

if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)




