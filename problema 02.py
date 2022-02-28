"""Com certeza deve haver uma melhor forma de escrever esse algoritmo, para os casos testes 
vai funcionar, porém acredito que se fosse um numero maior que 1080, ja daria erro"""

#entrada do angulo em float (real)
angulo = float(input("Digite um ângulo positivo: "))

#estrutura condicional para um angulo que seja maior e igual 0 e menor e igual a 360
if angulo >= 0 and angulo <= 360:
    if (angulo >= 0 and angulo <= 90):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo) ,"graus e está no quadrante 1")
    elif (angulo > 90 and angulo <= 180):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo) ,"graus e está no quadrante 2")
    elif (angulo > 180 and angulo <= 270):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo) ,"graus e está no quadrante 3")
    elif (angulo > 270 and angulo <= 360):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo) ,"graus e está no quadrante 4")

#estrutura condicional para um angulo maior que 360
if angulo > 360:
    angulo_reduzido = angulo - 360

    if (angulo_reduzido >= 0 and angulo_reduzido <= 90):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido) ,"graus e está no quadrante 1")
    elif (angulo_reduzido > 90 and angulo_reduzido <= 180):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido) ,"graus e está no quadrante 2")
    elif (angulo_reduzido > 180 and angulo_reduzido <= 270):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido) ,"graus e está no quadrante 3")
    elif (angulo_reduzido > 270 and angulo_reduzido <= 360):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido) ,"graus e está no quadrante 4")

if angulo > 720:
    angulo_reduzido2 = angulo - 720

    if (angulo_reduzido2 >= 0 and angulo_reduzido2 <= 90):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido2) ,"graus e está no quadrante 1")
    elif (angulo_reduzido2 > 90 and angulo_reduzido2 <= 180):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido2) ,"graus e está no quadrante 2")
    elif (angulo_reduzido2 > 180 and angulo_reduzido2 <= 270):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido2) ,"graus e está no quadrante 3")
    elif (angulo_reduzido2 > 270 and angulo_reduzido2 <= 360):
        print("O ângulo %.1f" %(angulo) ,"graus pode ser reduzido a %.1f" %(angulo_reduzido2) ,"graus e está no quadrante 4")