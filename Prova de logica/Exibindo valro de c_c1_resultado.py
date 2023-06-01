


def blevers():
    n=15    
    c = 0
    c1 = 1
    

    while c1<=n:
        if n%c1==0:
            c += 1
        c1 += 1
    
    print('Valor de c:', c)
    print('Valor de c1:', c1)

    return c

resultado = blevers()
print ('valor da função', resultado)

   
   

