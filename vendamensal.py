total = 0
vendas = []

for i in range(1, 7):
    venda = float(input(f"Vendas do mês {i}: "))
    vendas.append(venda)
    total += venda

media = total / 6

acima_da_media = 0
for venda in vendas:
    if venda > media:
        acima_da_media += 1

print("Total de vendas =", total)
print("Média mensal =", media)
print("Meses acima da média =", acima_da_media)
