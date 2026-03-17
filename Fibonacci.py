cont = 3
num1 = 0
num2 = 1

print(f"{num1}")
print(f"{num2}")

for cont in range(15):
    num3 = num1 + num2
    print(f"{num3}")
    num1 = num2
    num2 = num3
