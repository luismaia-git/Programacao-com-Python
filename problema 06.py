while True:
    N = int(input("Digite um número inteiro positivo: "))
    if N > 0:
        break

for i in range(1,N+1,1):
    if N % i == 0:
        print(i,"é divisor de",N)
        aux = i
        for d in range(1,aux+1,1):
            if aux > 1 and aux % d == 0 and aux != N:
                print(">",d, "é divisor de",aux)
  