print("======================")
print(" Contagem Inteligente ")
print("======================")

Inicio = int(input(" Inicio: "))
Final = int(input(" Final: "))
count = 1

if Final > Inicio:
    count = Inicio
    while count <= Final:
        print(count)
        count += 1

else:
    count = Inicio
    while count >= Final:
            print(count)
            count -= 1




