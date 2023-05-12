def tabuleiro(n):
    linha = 0
    while linha < n:
        coluna = 0
        while coluna < n:
            if (linha+coluna) % 2 == 0:
                print(2 * chr(9608), end ='')
            else:
                print(2* '', end='')    
            coluna += 1
        print (tabuleiro(n))
        linha += 1
