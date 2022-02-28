while True:
    base = float(input("Digite a base do triângulo: "))
    if base > 0:
        break
    else:
        print("Digite um valor positivo!")

while True:
    altura = float(input("Digite a altura do triângulo: "))
    if altura > 0:
        break
    else:
        print("Digite um valor positivo!")

area = (base * altura)/2

print("A área do triângulo é", area)