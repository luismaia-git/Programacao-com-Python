maior = 0
menor = 0
soma = 0
totalsoma = 0
produto = 1
while True:
    numero = float(input("Digite um número positivo: "))
    if numero > 0:
        soma = soma + numero
        totalsoma = totalsoma + 1 
        produto = produto * numero
        if numero > maior:
            maior = numero     

        if numero < menor:
            menor = numero    
    elif numero == 0:
        break

media = soma/totalsoma

print("A soma dos números é %.1f" %(soma))
print("A média dos números é %.1f" %(media))
print("O produto dos números é %.1f" %(produto))
print("O menor número digitado foi", menor)
print("O maior número digitado foi %.1f" %(maior))