#Crie um pograma que peça ao usuario preços de produtos comprados até que ele decida
#encerrar a compra. O programa, ao final, deve exibir o total gasto. 

total = 0
quero_comprar = True

while quero_comprar:
    preco = float(input('Preço: '))
    total += preco
    opcao = input('Continuar comprando (s/n)? ')
    if opcao != 's': #usuario digita qualquer coisa diferete de s
        quero_comprar = False 
print(f'Total da compra R$ {total:.2f}')
