largura=float(input('digite largura em mts'))
altura=float(input('digite altura em mts'))
area= largura*altura
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(largura, altura, area))

tinta= area/2
print('Para pintar esta parede você precisará de {}l de tinta'. format(tinta))
