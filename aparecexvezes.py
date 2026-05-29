n = input("Digite um número inteiro: ")
d = input("Digite um dígito (0-9): ")

contador = 0
for digito in n:
    if digito == d:
        contador += 1

print(f"O dígito {d} aparece {contador} vez(es)")
