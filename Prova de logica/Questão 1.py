#Convertendo o fluxograma apresentado para exibir a quantidade de resultados verdadeiros e valor de n1


def one():
    n1=37    
    n2 = 11 
    r = 1
    cont=0

    while r!=0:

        r=n1%n2
        n1=n2
        n2=r
        cont +=1
    print('valor de verdadeiro:', cont)    
    print('Valor de n1:', n1)
    

one()



   
   

