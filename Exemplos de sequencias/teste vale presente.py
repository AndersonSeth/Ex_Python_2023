vale_presente = float(input('Valor? '))
while vale_presente >0:
    mercadoria = float(input('Mercadoria? '))
    if mercadoria > vale_presente:
        print('Escolha outra')
        continue
    vale_presente -= mercadoria
print('Obrigado')