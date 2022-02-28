arq = open("vendas.txt", 'r')

extracao = {}

arq.readline()

for linha in arq.readlines():
    produto, quantidade, total = linha.strip().split(",")
    extracao[produto] = [ int(quantidade), int(total) ]
arq.close()
   
mais_uni = 0
mais_caro = 0
mais_barato = 99999
lista_vendas = []
produto_unidade = ''
produto_caro = ''
produto_barato = ''
total_vendas = 0

for produto, valores in extracao.items():   
    
    total_vendas = total_vendas + (valores[1])

    if valores[0] > mais_uni:
        mais_uni = valores[0]
        produto_unidade = produto
    if valores[1]/valores[0] > mais_caro:
        mais_caro = valores[1]/valores[0]
        produto_caro = produto
    if (valores[1]/valores[0]) < mais_barato:
        mais_barato = valores[1]/valores[0]
        produto_barato = produto

print(f"Produto com mais unidades vendidas: {produto_unidade}")
print(f"Produto mais caro: {produto_caro}")
print(f"Produto mais barato: {produto_barato}")
print(f"Valor total de vendas do supermercado: R${total_vendas:.2f}")
     
