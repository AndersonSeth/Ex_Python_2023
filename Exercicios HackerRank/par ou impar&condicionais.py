# n = int(input("Digite um numero"))
# if ((n%2) == 0) and n <=5:
#     print('Par')
# elif ((n%2) == 0) and (n >=6 <=20):
#     print('impar')
# else:
#     print('Impar')

n = int(input("Digite numero"))
if ((n%2) == 0 and n<=5):
    print ("Not Weird")
elif ((n%2) == 0) and (n>=6) and (n<=20):
    print ("Weird")
elif ((n%2) == 0) and (n>=20):
    print ("Not Weird")
else:
    print ("Weird")