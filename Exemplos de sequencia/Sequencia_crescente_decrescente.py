# n = int(input('Digite um numero: '))
# for i in range(1, n+1): #[1..n]
#     print (i, end=' ')

#Crie um programa que solicite um numero natural e exiba a sequencia crescente de zero 
#até o numero dado, somente pares:
# n = int(input('digite um numero: '))
# for i in range (0, n+1, 2): #2 para obter os pares
#     print(i, end=' ')

#Crie um programa que solicite um numero natural e exiba a sequencia decrescente do numero até um.

n = int(input('numero: '))
for i in range(n, 0, -1): #[n..0]
    print (i, end=' ')
