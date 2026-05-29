print("Digite 8 números inteiros:")

for i in range(8):
    numero = int(input(f"Número {i + 1}: "))
    
    if numero % 4 == 0:
        print(numero, "é divisível por 4")
