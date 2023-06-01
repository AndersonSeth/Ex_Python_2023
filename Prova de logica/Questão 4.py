
#Convertendo o fluxograma apresentado para exibir a quantidade de resultados verdadeiros

def quarta():
    n1=37    
    n2 = 11
    r=n1%n2 
    cont=0

    while r!=0:
        n1=n2
        n2=r
        r=n1%n2
        cont +=1

    print('valor de verdadeiro:', cont)    
    
    

quarta()



   
   

