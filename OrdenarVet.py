vet = list(range(4))

for i in vet:
    vet[i] = int(input(f"Digite o {i+1}o numero"))

for i in range(len(vet)):
    for j in range(len(vet) - 1 - i):
        if vet[j] > vet[j + 1]:
            vet[j], vet[j + 1] = vet[j + 1], vet[j]

print(vet)
