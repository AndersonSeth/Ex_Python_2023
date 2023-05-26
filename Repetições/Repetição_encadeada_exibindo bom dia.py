def exibe():
    i=0
    x=100
    y=200
    
    cont_dia = 0
    cont_tarde = 0
    cont_noite = 0
    while i<x:
        print('Bom dia')
        cont_dia +=1
        j=0       
        while j<y:      
            print('boa tarde')
            cont_tarde +=1
            j+=1
        i +=1
    print('boa noite')
    cont_noite += 1 

    print('Quantidades de Bom dia', cont_dia)
    print('Quanidade de boa tarde', cont_tarde)
    print('Quantidade de boa noite', cont_noite)

exibe()

   
   

