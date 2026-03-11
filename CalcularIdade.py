anoNasc = int(input("Digite o ano em que voce nasceu: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - anoNasc

if idade >= 18:
   {
       print(f"Voce ja tem {idade} anos, entao e maior de idade")
   }
else:
   print(f"Voce tem apenas {idade} anos, entao e menor de idade")


