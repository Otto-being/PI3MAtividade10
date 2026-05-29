total = 0
maior_consumo = 0
produto_maior = 0

for i in range(1, 8):
    consumo = float(input(f"Consumo de matéria-prima do produto {i} (kg): "))
    total += consumo
    
    if consumo > maior_consumo:
        maior_consumo = consumo
        produto_maior = i

print("Consumo total =", total, "kg")
print("Produto que consome mais:", produto_maior, "(", maior_consumo, "kg)")
