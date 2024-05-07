import requests
link="https://www.instagram.com/p/Cztmrd6MQ00/?utm_source=ig_web_copy_link"

resultado = requests.get(link)
print(resultado.text)