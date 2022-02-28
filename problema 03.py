dia_1 = int(input("Digite o dia da data1: "))
mes_1 = int(input("Digite o mês da data1: "))
ano_1 = int(input("Digite o ano da data1: "))

dia_2 = int(input("Digite o dia da data2: "))
mes_2 = int(input("Digite o mês da data2: "))
ano_2 = int(input("Digite o ano da data2: "))

#estrutura condicional para checar qual a data é maior
if ano_2 > ano_1:
    print("A data 2 é maior!")
elif ano_1 > ano_2:
    print("A data 1 é maior!")
elif ano_2 == ano_1:
    if mes_2 > mes_1:
        print("A data 2 é maior!")    
    elif mes_1 > mes_2:
        print("A data 1 é maior!")
    elif mes_2 == mes_1:
        if dia_2 > dia_1:
            print("A data 2 é maior!")
        elif dia_1 > dia_2:
            print("A data 1 é maior!")    
        elif dia_2 == dia_1:
            print("As datas são iguais!")    