#MEME

def meme():
    opcao = input('A bagaça funciona? S/N: ')
    if opcao in 'Ss':
        print('Nem rela ')
        print ('Sem problemas')
    
    elif opcao in "Nn":
        resposta = input('você que fudeu com o treco? S/n: ')   
        if resposta in "Ss":
            print ('Seu Imbecil') 
            resposta2 = input('Alguem sabe que foi você? S/N: ')
            if resposta2 in 'Ss':
                print ('Se Fodeu')
                resposta3 = input('Da para jogar a culpa em alguem? S/N: ')
                if resposta3 in 'Nn':
                    print('Se fodeu')
                elif resposta3 in "Ss":
                            print ('Sem problmas')
            if resposta2 in 'Nn':
               print('Esconda')       
               print('Sem problema')           
        if resposta in 'Nn':
             resposta4 = input("Alguem pode te culpar? S/N: ")
             if resposta4 in 'Ss':
                    print ('Se Fodeu')
                    resposta3 = input('Da para jogar a culpa em alguem? S/N: ')
                    if resposta3 in "Ss":
                            print ('Sem problmas')
                    elif resposta3 in "Nn":
                        print ('Se fodeu')
                
             elif resposta4 in 'Nn':
                    print ('então fodaSe')
                    print ('Sem problemas')                      

meme()

   

