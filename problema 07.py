lista = []
media = 0
for numero in range(5):
    lista.append(float(input("Digite uma nota: ")))
    media = media + lista[numero]
    
media = media/len(lista)
maximo = max(lista)
indicemax = lista.index(maximo) 
minimo = min(lista)
indicemin = lista.index(minimo) 


print("Média:", round(media,1))
print("Menor: nota", indicemin, "=", round(minimo,1)) 
print("Maior: nota", indicemax, "=", round(maximo,1)) 
