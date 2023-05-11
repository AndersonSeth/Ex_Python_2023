#Criar uma função que simule um relogio digital,
#exiba desde 00:00:00 até 23:59:59.

def relogio():
    h = 0
    while h < 24:
        m=0
        while m < 60:
            s = 0
            while s < 60:
                print(f'{h:02}:{m:02}:{s:02}')
                s += 1
            m += 1 
        h += 1
relogio()
