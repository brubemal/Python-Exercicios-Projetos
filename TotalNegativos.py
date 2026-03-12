# Total Negativos
qtdNum = int(input("Digite a quantidade de números que deseja inserir: "))
count = 0
TotalNegativos = 0

while True:
    num = int(input("Digite um número: "))
    count += 1
    if num < 0:
        TotalNegativos += 1

    if count > qtdNum:
        print(f"Quantidade de numeros negativos e: {TotalNegativos}")
        break
