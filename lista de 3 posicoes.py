#O código a seguir solicita ao usuário que seja digitado 
#números inteiros e os armazene em uma lista de 3 posições. 
#Substituindo todos os valores positivos e iguais a zero por 1 
#e todos os valores negativos por 0.

def troca(lista):
    for i in range (3):
        if lista [i]>= 0:
            lista[i] = 1
        else:
            lista[i] = 0
    return lista

lista = [0]*3
for i in range (3):
    lista [i] = int(input('Digite um valor: '))
print (lista)
troca(lista)
print(lista)