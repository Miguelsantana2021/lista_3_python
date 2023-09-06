base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente (deve ser um número inteiro): "))
resultado = 1
if expoente < 0:
    base = 1 / base
    expoente = -expoente
while expoente > 0:
    resultado *= base
    expoente -= 1
print("O resultado da potência é:", resultado)