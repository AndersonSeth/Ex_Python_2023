salario = float(input('Digite o salario: '))
tempo = int(input('Tempo de empresa em anos: '))
emprestimo = int (input('Valor desejado de emprestimo: '))


if salario > 2000:
        if tempo > 2:
                juros = emprestimo * 0.12
        if tempo < 2:
                juros = emprestimo*0.20
        print (f'O valor a pagar é ,{emprestimo:.2f},Mais os juros de, {juros:.2f}') 
else: 
        print ("Emprestimo negado")   