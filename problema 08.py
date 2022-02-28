#listas
lista_impar = []
lista_par = []

#par
menor_par = 0
maior_par = 0
media_par = 0

#impar
menor_impar = 0
maior_impar = 0
media_impar = 0

while True:
  numero = int(input("Digite um número inteiro: "))

  if numero == 0:
    break  
  elif numero%2 == 0:
    lista_par.append(numero)
    media_par = media_par + numero   
  elif numero%2 != 0:
    lista_impar.append(numero)
    media_impar = media_impar + numero

#operações com par
if len(lista_par) > 0:
  menor_par = min(lista_par)
  maior_par = max(lista_par)
  media_par = media_par/len(lista_par)

#operações com impar
if len(lista_impar) > 0:
  menor_impar = min(lista_impar)
  maior_impar = max(lista_impar)
  media_impar = media_impar/len(lista_impar)

#print par

if len(lista_par) == 0:
  print("Lista de pares vazia")
else:
  print("Menor par:", menor_par)
  print("Maior par:", maior_par)
  print("Média pares:", round(media_par,1))

#print impar


if len(lista_impar) == 0:
  print("Lista de ímpares vazia")
else:
  print("Menor ímpar:", menor_impar)
  print("Maior ímpar:", maior_impar)
  print("Média ímpares:", round(media_impar,1))