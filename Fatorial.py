count = 0
num = 1
fatorial = int(input("Digite um número para calcular seu fatorial: "))

while True:
    count += 1
    num *= count
    if count >= fatorial:
        print(f"O fatorial de {fatorial} é {num}")
        break