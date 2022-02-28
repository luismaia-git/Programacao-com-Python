'''Gostei desse problema!! Fiquei pensando muito na logica por trás de pegar os elementos da diagonal'''


tam_matriz = int(input("Digite a dimensão da matriz quadrada: "))

matriz =[]

for i in range(tam_matriz):
    linha = []
    for j in range(tam_matriz):
        linha.append(float(input(f"Elemento {i} x {j}: ")))
    matriz.append(linha)

print("Matriz digitada:")
for m in range(tam_matriz):
    print(matriz[m])

traço = 0
c = 0

for n in range(tam_matriz):
    
    traço = traço + matriz[n][c]
    c = c+1

print("Traço da matriz:",traço)