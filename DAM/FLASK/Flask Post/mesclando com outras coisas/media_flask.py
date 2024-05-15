from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/calc_media")

def calcular_media():
    numeros = [10, 20, 30, 40, 50]
    total = sum(numeros)
    media = total / len(numeros)
    print("A média é:", media)
    return jsonify(media)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)