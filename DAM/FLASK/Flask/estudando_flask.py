from flask import Flask


app = Flask(__name__)


@app.route("/")
# @app.route("/bom-dia")# podemos definir o local que vai aparecer nossa função 

def boasVindas():
    return 'bom dia'

@app.route("/um/caminho/com/varios/elementos") #entendendo caminhos 
def um_caminho_longo():
    return 'Bom dia'


if __name__=="__main__":
    app.run()
    # app.run(host='localhost', port=5002, debug=True) #Podemos definir a porta do servidor local 




