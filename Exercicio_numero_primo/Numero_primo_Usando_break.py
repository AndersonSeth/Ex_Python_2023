#Crie um programa que receba um numero natural n(n>1)
#e exiba uma mensagem indicado se n é primo.
n=int(input('digite um Número: '))
divisor = 2
while divisor < n:
    print(f'{n} % {divisor} = {n % divisor}')
    if n % divisor == 0:
        break
    divisor += 1 
if divisor == n:
    print('O numero é primo')
else:
    print('Não é primo')