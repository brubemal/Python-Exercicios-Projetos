vet = list(range(4))

for i in vet:
    vet[i] = int(input(f"Digite o {i+1}o numero"))

for i in range(len(vet)):
    for j in range(i + 1, len(vet)):
        if vet[i] > vet[j]:
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

print(vet)
