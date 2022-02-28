valores = {}

notas = []

def preencher_dicionario(valores, notas):
    


    nota = input("Quais os valores de notas do seu cofre? ")
    notas = nota.split(',')
    
    
    for x in range(len(notas)):
        valores[notas[x]] = int(input(f"Quantidade de notas de R${notas[x]}: "))
        
    
    lista_valores = []
    for value in valores.values():
        lista_valores.append(value)
   
    total = 0

    for i in range(len(notas)):
        total = total + (int(notas[i])*lista_valores[i])
    


    mostrar_dicionario(valores, notas, lista_valores, total)



def mostrar_dicionario(valores, notas, lista_valores, total):

    print("Estado do cofre")
    for valor in range(len(valores)):
        print(f"Notas de R${notas[valor]}: ",lista_valores[valor])
        
    print(f"Total no cofre: R${total:.2f}")    


preencher_dicionario(valores, notas)