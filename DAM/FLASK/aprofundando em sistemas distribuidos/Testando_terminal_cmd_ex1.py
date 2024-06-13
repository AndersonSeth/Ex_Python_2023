from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def boasVindas():
    nome = request.get_json(force=True)
    return 'Seja Bem-vindo, {}, na aula de DEV API. \n'. format(nome['nome'])

if __name__ == '__main__':
    app.run(host= 'localhost', port = 5002, debug = True)

# No segundo terminal digitamos: 
# curl -H \Content-Type:application/json\ -X POST --data "{\"nome\":\"Andreia\"}" http://localhost:5002/  