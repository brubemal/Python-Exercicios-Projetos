print("======================")
print("   Escola  Generica   ")
print("======================")
qtdAluno = int(input("Digite quantos alunos tem na escola? "))
count = 1
melhorNota = 0
media = 0

while count <= qtdAluno:
    nome = input(f"Digite o nome do aluno {count}: ")
    nota = float(input(f"Digite a nota do aluno {count}: "))

    if nota > melhorNota:
        melhorNota = nota
        melhorAluno = nome

    count += 1
    media += nota

media = media/qtdAluno

print(f"Melhor aluno: {melhorAluno}")
print(f"Melhor nota: {melhorNota}")
print(f"Media das notas da sala: {media}")
