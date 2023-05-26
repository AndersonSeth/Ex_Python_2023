# idades = [45, 67, 12, 30, 51, 24]
# tamanho = len (idades)
# idades [tamanho ] += 1 #erro na 3 pois não passamos valor entre as chaves
# print (idades)

def contagem_progressiva(n):
    for i in range (0,n+1):
        print(i)

def contagem_regressiva(n):
    for i in range(n,0,-1):
        print(i)

x = int(input('X? '))
opcao = input('Opção? ')
if opcao in 'Pp':
    contagem_progressiva(x)
else:
    contagem_regressiva(x)
