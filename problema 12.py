

def cria_matriz_identidade(d):
    
    matriz = []

    for j in range(d):
        linha = []
        for k in range(d):
            if j == k:
                linha.append(1)
            else:
                linha.append(0)       
            
        matriz.append(linha)
          
    mostra_matriz(matriz,d)

def mostra_matriz(matriz,d):
    print(f"Matriz identidade {d}x{d}:")
    for linha in matriz:
        print(linha)


entradas = []

entradas.append([int(x) for x in input("Digite o intervalo: ").split(',') ])

A = entradas[0][0]
B = entradas[0][1]

#intervalo 
for d in range(A,B+1):

   cria_matriz_identidade(d)

   

