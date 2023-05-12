#Crie um programa que receba como entrada o crédito de um cliente e depois o preço de itens
#comprados por esse cliente, o programa deverá parar de solicitar novos preços
#quando o crédito disponivel for insuficiente para para um dos itens. Ao final
#exiba o credito restante;
credito = float (input('Seu crédito: R$ '))
while credito >0:
    item = float(input('Preço do item: R$'))
    if item > credito:
        print(f'Compra negada! Restam :R$ {credito:.2f} ')
        continue
    credito -= item
print('Você consumiu todo seu credito')

