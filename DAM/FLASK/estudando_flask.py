from flask import Flask


app = Flask(__name__)


@app.route("/")
def boasVindas():
    return 'Seja bem-vindo'

if __name__=="__main__":
    app.run()

