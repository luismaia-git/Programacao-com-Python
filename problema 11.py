entradas = []

entradas.append([int(x) for x in input("Digite a dimensão da matriz: ").split(',') ])

l = entradas[0][0]
c = entradas[0][1]

matriz = []
for i in range(l):
    matriz.append([float(x) for x in input(f"Digite a linha {i}: ").split(',') ])

print("Matriz digitada:")
for linha in matriz:
    print(linha)

n_par = 0
n_impar = 0

for i in range(l):
    for j in range(c):
        if matriz[i][j]%2 == 0:
            n_par = n_par + 1
        else:
            n_impar = n_impar + 1

print("Números pares:", n_par) 

print("Números ímpares:", n_impar) 
