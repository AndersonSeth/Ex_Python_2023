from flask import Flask, make_response, jsonify, redirect
app = Flask(__name__)

@app.route("/exemplo5")
def exemplo5():
    x = jsonify(["pêra", "maçã", "laranja"])
    r = make_response(x)
    r.headers["X-tipo-dado"] = "frutas"
    r.status_code = 275
    return r

@app.route("/exemplo6")
def exemplo6():
    # Se code fosse omitido, o 302 seria utilizado por padrão.
    return redirect("/exemplo5", code = 305)

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000, debug=True)