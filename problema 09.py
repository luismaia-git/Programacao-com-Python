
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print("Frase digitada:",frase)
print("Palavra digitada:", palavra)

i = 0

while i >= 0:
    i = frase.find(palavra, i)
    if i >=0:
        print(palavra,"aparece na posição", i)
        i = i+1
