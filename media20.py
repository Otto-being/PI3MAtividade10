soma = 0

for i in range(20):
    valor = float(input(f"Digite o valor {i + 1}: "))
    soma += valor

media = soma / 20
print("Média =", media)
