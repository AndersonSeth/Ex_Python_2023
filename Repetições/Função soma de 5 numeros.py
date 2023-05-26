
def soma():
    soma=0
    cont=1

    while cont<=5:
        num=int(input('Digite os numeros'))
        soma=soma+num
        cont=cont+1
    
    return soma
resultado = soma()
print('A soma é', resultado)
    

   

