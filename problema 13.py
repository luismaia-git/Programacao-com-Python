n_disc = int(input('Qual o número de disciplinas? '))

lista = []

dicionario_inicial = {'disciplina': [], 'nota1':[], 'nota2':[], 'nota3': [], 'media':[]}

def inserir_no_dicionario(dicionario_inicial, lista):
    
    dicionario_completo = dicionario_inicial
    
    nome = input("Qual o nome da disciplina? ")
    
    notas = []
    nota = input("Digite as 3 notas da disciplina separadas por vírgulas: ")
    notas.append(nota.split(',')) 

    

    dicionario_completo['nota1'].append(float(notas[0][0]))
    dicionario_completo['nota2'].append(float(notas[0][1]))
    dicionario_completo['nota3'].append(float(notas[0][2]))

    media = (float(notas[0][0]) + float(notas[0][1]) + float(notas[0][2])) / 3

    dicionario_completo['media'].append(media)
    dicionario_completo['disciplina'].append(nome)

    lista.append(dicionario_completo)


def mostrar_notas(lista):
    for x in range(len(lista)):
        print(lista[x]['disciplina'][x])
        print(f"Nota 1: {lista[x]['nota1'][x]:.1f}")
        print(f"Nota 2: {lista[x]['nota2'][x]:.1f}")
        print(f"Nota 3: {lista[x]['nota3'][x]:.1f}")
        print(f"Média: {lista[x]['media'][x]:.1f}")
       


for x in range(n_disc):
    inserir_no_dicionario(dicionario_inicial,lista)
    
mostrar_notas(lista)
    



