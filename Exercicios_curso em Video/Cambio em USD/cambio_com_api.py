import requests

# Função para obter a cotação do dólar
def obter_cotacao():
    url = "https://v6.exchangerate-api.com/v6/ff1e6a8352d76435f965971d/latest/BRL"  
    response = requests.get(url)
    dados = response.json()
    cotacao_dolar = dados['conversion_rates']['USD']
    return 1 / cotacao_dolar

# Solicitar o valor em reais
real = float(input('Quanto dinheiro você tem na carteira? R$ '))

# Obter cotação atual do dólar
try:
    cotacao_dolar = obter_cotacao()
    dolar = real / cotacao_dolar
    print(f'A cotacao atual é {cotacao_dolar:.2f} USD para 1 BRL')
    
    print(f'Com R$ {real:.2f}, você pode comprar US$ {dolar:.2f}. A cotacao atual é {cotacao_dolar:.2f}')
except Exception as e:
    print(f"Ocorreu um erro ao obter a cotação: {e}")