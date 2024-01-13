prod = float(input('Quando custa o produto? R$'))
desc = prod*5/100
print('O valor do produto é R$ {:.2f},com 5% de desconto o valor fica em R$ {:.2f}'.format(prod,(prod-desc)))