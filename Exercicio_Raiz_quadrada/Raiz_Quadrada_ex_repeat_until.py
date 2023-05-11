#Crie um programa que receba um número n>=0 e exiba o valor da 
#Raiz Quadrada de n. Enquanto n for um umero negativo, repita a solicitação de entrada

from math import sqrt

while True:
    n = float(input('Digite um numero >0 para exibir sua raiz quadrada: '))
    if n >= 0: break 

print(f'Raiz quadrade de {n} é {sqrt(n)}')
