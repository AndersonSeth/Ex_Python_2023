import requests 

nome = input("digite o nome: ")
sexo = input("digite o sexo: ")
cabelo = input("digite a cor do cabelo: ")

dados = {"nome": nome, "sexo": sexo, "cabelo": cabelo}

x = requests.post("http://localhost:5000/pessoa", json = dados)
if x.status_code != 200:
    print(f"[{x.status_code}] {x.text}")
else:
    print(x.text)