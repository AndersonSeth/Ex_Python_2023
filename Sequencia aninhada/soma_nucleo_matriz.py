matriz= [
    [68,86,50,42,84,98,75],
    [15,83,10,16,14,99,58],
    [30,68,78,44,70,25,31],
    [69,53,17,87,55,83,15],
    [20,70,78,61,65,16,26],
]

linhas=len(matriz)
colunas=len(matriz[0])

def soma_nucleo1(M,L,C):
    soma = 0
    for i in range(1,L):
        for j in range(1,C):
            soma += M[i][j]
    return soma

def soma_nucleo2(M,L,C):
    soma = 0
    for i in range(1,L-1):
        for j in range(1,C-1):
            soma += M[i][j]
    return soma

def soma_nucleo3(M,L,C):
    soma = 0
    for i in range(2,L-1):
        for j in range(2,C-1):
            soma += M[i][j]
    return soma

#A SOMA DO NUCLEO É 802 OBJETIVO ENCONTRAR A FUNÇÃO CORRETA

print(f'Soma nucleo 1 = {soma_nucleo1(matriz, linhas, colunas)}')
print(f'Soma nucleo 2 = {soma_nucleo2(matriz, linhas, colunas)}')
print(f'Soma nucleo 3 = {soma_nucleo3(matriz, linhas, colunas)}')

