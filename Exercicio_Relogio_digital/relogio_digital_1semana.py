from time import sleep
dias = 7
while dias > 0:
    for h in range (24):
        for m in range (60):
            for s in range (60):
                print (f'{h:02}:{m:02}:{s:02}')
                sleep(1)
    dias +=1 #decrementar para considerar 1 semana
