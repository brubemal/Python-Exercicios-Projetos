AC1 = float(input("Digite sua nota da AC1: "))
AC2 = float(input("Digite sua nota da AC2: "))
AF = float(input("Digite sua nota da AF: "))
AG = float(input("Digite sua nota da AG: "))
NotaFinal = (AC1 * 0.15) + (AC2 * 0.3) + (AF * 0.45) + (AG * 0.1)

if NotaFinal >= 8:
    print(f"Sua nota foi {NotaFinal}, voce esta de parabens! ")

elif NotaFinal >= 5 and NotaFinal <= 7.9:
    print(f"Sua nota foi {NotaFinal}, voce passou!")

elif NotaFinal <= 4.9 and NotaFinal >= 4:
    print(f"Sua nota foi {NotaFinal}, voce reprovou por pouco.")

else:
    print(f"Sua nota foi {NotaFinal}, voce esta reprovado, precisa melhorar.")