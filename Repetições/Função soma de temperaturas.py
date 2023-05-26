
def somatemp():
    soma=0
    cont=1

    while cont<=30:
        temp=float(input('digite temperatura'))
        soma=soma+temp
        cont=cont+1
    
    return soma
resultado = somatemp()
print('A soma das emperaturas é', resultado)
    

   

