print("[1]Doar 10")
print("[2]Doar 20")
print("[3]Doar 30")
print("[4]Doar outro valor")
print("[5]Cancelar")

opcao = int(input("Qual opcoe voce deseja? "))
valor = 0 

match opcao:
    case 1:
        valor = 10
    
    case 2: 
        valor = 20

    case 3:
        valor = 30

    case 4:
        valor = int(input("Digite o valor que deseja doar: "))
    
    case _:
        valor = 0


