altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kilos: "))

IMC = peso/altura ** 2

if IMC >= 18.5 and IMC <= 25:
   print(f"Seu IMC e {IMC} e voce esta no nivel normal")

elif IMC < 18.5:
   print(f"Seu IMC e {IMC} e voce esta no nivel de magreza")

else:
   print(f"O seu IMC e {IMC} e voce esta no nivel de sobrepeso")