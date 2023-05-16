n= int (input('n? '))

comeco = 0
final = n
passo = -1

for i in range(comeco, final):
    print (i, end=' ')
print ()

for i in range (final-1, comeco-1, passo):
    print(i, end= ' ')