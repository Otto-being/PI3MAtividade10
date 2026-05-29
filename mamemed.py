maior = None
menor = None
soma = 0

for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    
    if i == 0:
        maior = numero
        menor = numero
    
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    
    soma += numero

media = soma / 5

print("Maior número =", maior)
print("Menor número =", menor)
print("Média aritmética =", media)
