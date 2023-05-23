#Tabuada 1 ao 6

def tabuada():
    tab=1
    while tab<=6:
        i=1
        while i<=10:
            print(tab,"x", i, "=",tab*i)
            i+=1
        
        tab=tab+1

    return
tabuada()
