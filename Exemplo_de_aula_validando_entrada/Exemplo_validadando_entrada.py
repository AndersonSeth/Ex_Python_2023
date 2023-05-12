def somatorio (n):
    soma = 0
    natural = 1
    while natural <= n:
        soma += natural
        natural +=1
    return soma

while True:
    n= int(input('Digite um numero natural entre 0 e 100: '))
    if 0 <= n <= 100: break
print (f'a soma dos {n} primeiros naturais é {somatorio(n)}.')