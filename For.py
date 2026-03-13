cont = 1
qtdEntre = 0
somaImp = 0
qtd = int(input("Digite quantos numeros deseja: "))

for cont in range(qtd):
    valor = int(input("Digite um valor: "))
    if valor >= 0 and valor <= 10:
        qtdEntre += 1
        if valor % 2 == 1:
            somaImp += valor

print(f"A quantidade de numeros entre 0 e 10 e: {qtdEntre}")
print(f"A soma dos numeros impares entre 0 e 10 e: {somaImp}")