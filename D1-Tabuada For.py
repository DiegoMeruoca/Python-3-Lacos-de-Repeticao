lista = range(0, 11)
num1 = int(input("Digite o número da tabuada desejada:"))  # Recebe o numero
for posicao in lista:
    result = num1 * posicao  # Resultado recebe o numero vezes o valor atual de x
    print("{} X {} = {}" .format(num1, posicao, result))  # Exibe os valores na tela